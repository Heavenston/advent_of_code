use std::{fs, mem::size_of};
use arrayvec::ArrayVec;
use itertools::{ Itertools, iproduct };
use std::collections::{ HashMap, HashSet, VecDeque, BinaryHeap };
use nalgebra as na;

#[derive(Hash, Debug, Clone)]
struct Valve<'a> {
    name: &'a str,
    rate: u16,
    conns: Vec<&'a str>,
}

#[derive(Hash, Debug, Clone, Copy, PartialEq, Eq)]
struct State {
    pressure: u16,
    minutes: u8,
    opened: [u8; 7],

    pos1: u8,
    pos2: u8,
    wait2: u8,
}

impl State {
    pub fn is_opened(&self, pos: u8) -> bool {
        (self.opened[(pos / 8) as usize] & (1 << (pos % 8))) != 0
    }

    pub fn open(&mut self, pos: u8) {
        self.opened[(pos / 8) as usize] |= 1 << (pos % 8);
    }

    pub fn opened(&self) -> u8 {
        self.opened.iter().map(|a| a.count_ones() as u8).sum()
    }
    
    pub fn flow(&self, vls: &[Valve]) -> u16 {
        (0..vls.len())
            .filter(|i| self.is_opened(*i as u8))
            .map(|p| vls[p].rate)
            .sum()
    }

    pub fn with_pos(&self, pos: u8, wait: u8, vls: &[Valve]) -> Self {
        let mut n = *self;
        n.set_pos(pos, wait, vls);
        n
    }
    pub fn set_pos(&mut self, pos: u8, mut wait: u8, vls: &[Valve]) {
        self.pos1 = pos;

        if self.wait2 > wait {
            self.pressure += self.flow(vls) * wait as u16;
            self.minutes -= wait;
            self.wait2 -= wait;
        }
        else {
            wait -= self.wait2;
            self.pressure += self.flow(vls) * self.wait2 as u16;
            self.minutes -= self.wait2;
            self.wait2 = wait;
            std::mem::swap(&mut self.pos1, &mut self.pos2);
        }
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}
impl Ord for State {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        if self.minutes == other.minutes {
            self.pressure.cmp(&other.pressure)
        }
        else {
            self.minutes.cmp(&other.minutes)
        }
    }
}

fn main() {
    let contents = fs::read_to_string("../test.txt").unwrap();

    let mut vls: Vec<Valve> = contents.lines().map(|l| {
        let (part1, part2) = l.split(";").collect_tuple().unwrap();
        // rate = int(part1.split(" ")[4].split("=")[1])
        // conns = part2.split(", ")
        // conns[0] = conns[0][-2:]

        let mut conns = part2.split(", ").collect_vec();
        conns[0] = &conns[0][conns[0].len()-2 ..];
        let name = part1.split(" ").nth(1).unwrap();

        Valve {
            name,
            rate: part1.split(" ").nth(4).unwrap().split("=").nth(1).unwrap().parse().unwrap(),
            conns,
        }
    }).collect();
    let mut connections = vls.iter().map(|v| v.conns.iter().map(|conn|
        (vls.iter().enumerate().find(|a| &a.1.name == conn).unwrap().0 as u8, 1)
    ).collect_vec()).collect_vec();

    // Graph Pruning
    println!("Pruning...");
    let mut removed_vls = HashSet::<usize>::new();
    'outer: while true {
        for i in 0..vls.len() {
            if vls[i].rate != 0 { continue }
            if removed_vls.contains(&i) { continue }

            removed_vls.insert(i);

            for j in 0..vls.len() {
                // if removed_vls.contains(&j) { continue }

                let culprit = connections[j].iter()
                    .copied()
                    .enumerate().find(|(_, (a, _))| *a == i as u8);
                if let Some((index, (_, cost))) = culprit {
                    let mut nc = connections[j].clone();
                    nc.remove(index);
                    nc.extend(
                        connections[i].iter().copied()
                        .filter(|(a, _)| *a != j as u8)
                        .map(|(a, b)| (a, b + cost))
                    );
                    let mut g = HashMap::new();
                    for (a, b) in nc {
                        if let Some(d) = g.get_mut(&a) {
                            *d = b.min(*d);
                        }
                        else {
                            g.insert(a, b);
                        }
                    }
                    connections[j] = g.into_iter().collect_vec();
                }
            }

            continue 'outer;
        }
        break;
    }
    println!("Pruned {} valves: {removed_vls:?}", removed_vls.len());
    // println!("{connections:#?}");

    let start = vls.iter().enumerate()
        .find(|a| a.1.name == "AA").unwrap().0;
    // connections[start] = connections[start].iter().copied()
    //     .filter(|a| vls[a.0 as usize].rate != 0).collect();
    let starts = [(start as u8, 0)]
        .into_iter().collect_vec();

    {
        let mut f = HashMap::<u8, u8>::new();
        f.extend(starts.iter().copied());

        let mut a = starts.clone();
        while let Some((b, c)) = a.pop() {
            let n = connections[b as usize].iter().cloned()
                .filter(|(k, cost)| f.get(&k).map(|&pc| pc+c < *cost).unwrap_or(true))
                .map(|(k, cost)| (k, cost+c))
                .collect_vec();
            n.iter().copied().for_each(|(k, v)| { f.insert(k, v); });
            a.extend(&n);
        }
        println!("<accessible>");
        for (k, v) in f {
            if vls[k as usize].rate == 0 { continue }
            println!("{k} = {v} -> {}", vls[k as usize].name);
        }
        println!("</accessible>");

        println!("<state>");
        for (i, v) in vls.iter().enumerate() {
            if v.rate == 0 { continue }
            println!("Valve {} has flow rate={}; tunnels lead to valves {}",
                v.name, v.rate,
                connections[i].iter().copied()
                .map(|(a, b)| format!("({}, {})", vls[a as usize].name, b))
                .join(", ")
            );
        }
        println!("</state>");
    }

    let mut heap = BinaryHeap::<State>::new();
    for (start, cost) in starts {
        heap.push(State {
            pressure: 0,
            minutes: 25 - cost,
            opened: Default::default(),

            pos1: start,
            pos2: start,
            wait2: 0,
        });
    }

    let mut parkoured = HashSet::<State>::new();

    let mut i = 0;
    while heap.len() > 0 {
        let mut state = heap.pop().unwrap();
        if i % 100000 == 0 {
            println!("{}", parkoured.len());
            println!("{}", heap.len());
            println!("{}", state.minutes);
            println!("{}", state.wait2);
            println!("---------");
        }
        i += 1;

        if state.minutes <= 0 {
            let pressure =
                state.pressure + state.flow(&vls) * state.minutes as u16;
            println!("<finished>");
            println!("Parkoured > {}", parkoured.len());
            println!("SOLutioN  > {pressure}");
            println!("</finished>");
            return;
        }

        if state.opened() as usize >= vls.len() {
            state.pressure += state.flow(&vls) * state.minutes as u16;
            state.minutes = 0;

            if !parkoured.contains(&state) {
                heap.push(state);
                parkoured.insert(state);
            }
            continue;
        }

        let pos = state.pos1;
        let v = &vls[pos as usize];

        if state.minutes >= 1 && v.rate != 0 && !state.is_opened(pos) {
            let mut s = state.clone();
            s.open(pos);
            s.set_pos(pos, 1, &vls);
            if !parkoured.contains(&s) {
                parkoured.insert(s);
                heap.push(s);
            }
        }

        for &(conn, cost) in &connections[pos as usize] {
            if state.minutes < cost { continue }

            let s = state.with_pos(conn, cost, &vls);
            if parkoured.contains(&s) {
                continue
            }
            parkoured.insert(s);
            heap.push(s);
        }
    }
}

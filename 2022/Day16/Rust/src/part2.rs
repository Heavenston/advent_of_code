use std::fs;
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

#[derive(Hash, Debug, Clone, PartialEq, Eq)]
struct State {
    position: [(u8, u16); 2],
    pressure: u16,
    minutes: u8,
    opened: Vec<u16>,
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
        (vls.iter().enumerate().find(|a| &a.1.name == conn).unwrap().0 as u16, 1)
    ).collect_vec()).collect_vec();

    // Graph Pruning
    println!("Pruning...");
    let mut removed_vls = HashSet::<usize>::new();
    'outer: while false {
        for i in 0..vls.len() {
            if vls[i].rate != 0 { continue }
            if removed_vls.contains(&i) { continue }

            removed_vls.insert(i);

            for j in 0..vls.len() {
                // if removed_vls.contains(&j) { continue }

                let culprit = connections[j].iter()
                    .copied()
                    .enumerate().find(|(_, (a, _))| *a == i as u16);
                if let Some((index, (_, cost))) = culprit {
                    let mut nc = connections[j].clone();
                    nc.remove(index);
                    nc.extend(
                        connections[i].iter().copied()
                        .filter(|(a, _)| *a != j as u16)
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
    let starts = [(start as u16, 0)]
        .into_iter().collect_vec();

    {
        let mut f = HashMap::<u16, u8>::new();
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
            position: [(0, start), (0, start)],
            pressure: 0,
            minutes: 25 - cost,
            opened: Default::default(),
        });
    }

    let mut parkoured = HashSet::<State>::new();

    let mut i = 0;
    while heap.len() > 0 {
        let mut state = heap.pop().unwrap();
        if i % 100000 == 0 {
            println!("{}", heap.len());
            println!("{}", state.minutes);
            println!("{:?}", state.position);
            println!("---------");
        }
        i += 1;

        let pressure_per_min = state.opened.iter().map(|&p| vls[p as usize].rate).sum::<u16>();
        let min_wait = state.position.iter().copied().enumerate()
            .min_by_key(|a| a.1.0).unwrap();

        if state.minutes <= min_wait.1.0 {
            let pressure =
                state.pressure + pressure_per_min * state.minutes as u16;
            println!("> {pressure}");
            return;
        }

        if min_wait.1.0 > 0 {
            state.position[0].0 -= min_wait.1.0;
            state.position[1].0 -= min_wait.1.0;
            state.minutes -= min_wait.1.0;
            state.pressure += pressure_per_min * min_wait.1.0 as u16;
        }

        if state.opened.len() >= vls.len() {
            heap.push(state);
            continue;
        }

        let (_, pos) = state.position[min_wait.0];
        let v = &vls[pos as usize];

        if v.rate != 0 && !state.opened.contains(&pos) {
            let mut h = state.opened.clone();
            h.push(pos);
            h.sort_unstable();

            let mut np = state.position.clone();
            np[min_wait.0].0 = 1;

            let s = State {
                opened: h,
                position: np,
                ..state.clone()
            };
            if !parkoured.contains(&s) {
                parkoured.insert(s.clone());
                heap.push(s);
            }
        }

        for &(conn, cost) in &connections[pos as usize] {
            let mut np = state.position.clone();
            np[min_wait.0] = (cost, conn);
            let s = State {
                position: np,
                ..state.clone()
            };
            if parkoured.contains(&s) {
                continue
            }
            parkoured.insert(s.clone());
            heap.push(s);
        }
    }
}

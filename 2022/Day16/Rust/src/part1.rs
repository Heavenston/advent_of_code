use std::fs;
use arrayvec::ArrayVec;
use itertools::{ Itertools, iproduct };
use std::collections::{ HashMap, HashSet, VecDeque, BinaryHeap };
use nalgebra as na;

#[derive(Hash, Debug, Clone)]
struct Valve<'a> {
    name: &'a str,
    rate: u32,
    conns: Vec<&'a str>,
}

#[derive(Hash, Debug, Clone)]
struct State<'a> {
    position: &'a str,
    pressure: u32,
    minutes: u8,
    opened: Vec<&'a str>,
}

impl<'a> PartialEq for State<'a> {
    fn eq(&self, other: &Self) -> bool {
        self.pressure == other.pressure
    }
}
impl<'a> Eq for State<'a> {  }
impl<'a> PartialOrd for State<'a> {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}
impl<'a> Ord for State<'a> {
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
    let contents = fs::read_to_string("../input.txt").unwrap();

    let vls: HashMap<&str, Valve> = contents.lines().map(|l| {
        let (part1, part2) = l.split(";").collect_tuple().unwrap();
        // rate = int(part1.split(" ")[4].split("=")[1])
        // conns = part2.split(", ")
        // conns[0] = conns[0][-2:]

        let mut conns = part2.split(", ").collect_vec();
        conns[0] = &conns[0][conns[0].len()-2 ..];
        let name = part1.split(" ").nth(1).unwrap();

        (name.clone(), Valve {
            name,
            rate: part1.split(" ").nth(4).unwrap().split("=").nth(1).unwrap().parse().unwrap(),
            conns,
        })
    }).collect();

    let mut heap = BinaryHeap::<State>::new();
    heap.push(State {
        position: "AA".into(),
        pressure: 0,
        minutes: 29,
        opened: Default::default(),
    });

    let mut parkoured = HashSet::<State>::new();

    let mut i = 0;
    while heap.len() > 0 {
        let mut state = heap.pop().unwrap();
        i += 1;
        if i % 10000 == 0 {
            println!("{}", heap.len());
            println!("{}", state.minutes);
            println!("---------");
        }

        if state.minutes <= 0 {
            println!("> {state:#?}");
            return;
        }

        let v = &vls[&state.position];
        state.pressure += state.opened.iter().map(|p| vls[p].rate).sum::<u32>();

        if v.rate != 0 && !state.opened.contains(&state.position) {
            let mut h = state.opened.clone();
            h.push(state.position.clone());
            h.sort();
            let s = State {
                opened: h,
                pressure: state.pressure + v.rate,
                minutes: state.minutes-1,
                ..state.clone()
            };
            if !parkoured.contains(&s) {
                parkoured.insert(s.clone());
                heap.push(s);
            }
        }

        for conn in &v.conns {
            let s = State {
                minutes: state.minutes-1,
                position: conn,
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

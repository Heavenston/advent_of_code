use std::fs;
use std::iter::Iterator;

fn day2(lines: &[&str]) -> u32 {
    let mut horizontal = 0;
    let mut depth = 0;
    for line in lines {
        let (action, param) = line.split_once(' ').unwrap();
        let x = param.parse::<u32>().unwrap();
        match action {
            "forward" => horizontal += x,
            "down" => depth += x,
            "up" => depth -= x,
            _ => ()
        }
    }
    return horizontal * depth;
}

fn main() {
    let input = fs::read_to_string("../input.txt").unwrap();
    let lines = input.lines().collect::<Vec<_>>();

    println!("{}", day2(&lines));
}

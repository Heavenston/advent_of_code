use std::fs;
use std::iter::Iterator;

fn part1(numbers: &[u32]) -> u32 {
    (0..(numbers.len() - 1))
        .filter(|&i| numbers[i] < numbers[i + 1])
        .count() as u32
}

fn main() {
    let input = fs::read_to_string("../input.txt").unwrap();
    let numbers = input.lines().filter_map(|a| a.parse::<u32>().ok()).collect::<Vec<_>>();

    let result = part1(&numbers);

    println!("{}", result);
}

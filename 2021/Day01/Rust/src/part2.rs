use std::fs;
use std::iter::Iterator;

fn part1(numbers: &[u32]) -> u32 {
    (0..(numbers.len() - 1))
        .filter(|&i| numbers[i] < numbers[i + 1])
        .count() as u32
}

fn part2(numbers: &[u32]) -> u32 {
    let windows = (0..(numbers.len() - 2))
        .map(|i| (0..=2).map(|d| numbers[i + d]).sum::<u32>())
        .collect::<Vec<_>>();
    part1(&windows)
}

fn main() {
    let input = fs::read_to_string("../input.txt").unwrap();
    let numbers = input.lines().filter_map(|a| a.parse::<u32>().ok()).collect::<Vec<_>>();

    let result = part2(&numbers);

    println!("{}", result);
}

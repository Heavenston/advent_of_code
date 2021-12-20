use std::fs;
use arrayvec::ArrayVec;
use itertools::{ Itertools, iproduct };
use std::collections::{ HashMap, HashSet, VecDeque };
use nalgebra as na;

type ImageLine = VecDeque<u16>;
type Image = VecDeque<ImageLine>;

fn print_image(image: &Image) {
    for line in image.iter() {
        println!("{}", line.iter().copied().map(|a| if a == 0 { '.' } else { '#' }).collect::<String>());
    }
}

fn algo_step(input: &Image, input_infinity: u16, algo: &[u16]) -> (Image, u16) {
    const SIZE_DIFF: usize = 2;

    let mut output = Image::with_capacity(input.len()+SIZE_DIFF);
    for _ in 0..(input.len() + SIZE_DIFF) {
        output.push_front(ImageLine::from(vec![0; input[0].len()+SIZE_DIFF]));
    }

    macro_rules! get_pixel {
        ($x: expr => $dx: expr, $y: expr => $dy: expr) => {{
            input
                .get(($dy - (SIZE_DIFF as isize / 2) + $y as isize) as usize)
                .map(|a| a.get(($dx - (SIZE_DIFF as isize / 2) + $x as isize) as usize))
                .flatten().copied().unwrap_or(input_infinity)
        }};
    }

    for x in 0..output[0].len() {
        for y in 0..output.len() {
            let p = (-1..=1)
                .cartesian_product(-1..=1)
                .map(|(dy, dx)| get_pixel!(x => dx, y => dy))
                .collect::<ArrayVec<_, 9>>();
            let s = p.iter().fold(0, |acc, &x| acc*2 + x);

            output[y][x] = algo[s as usize];
        }
    }

    println!("Output = ");
    print_image(&output);
    println!("=> {}", input_infinity);
    return (output, if input_infinity == 1 { algo[algo.len() - 1] } else { algo[0] });
}

fn main() {
    let contents = fs::read_to_string("../input.txt").unwrap();
    let (algo_text, image_text) = contents.split_once("\n\n").unwrap();

    let algo = algo_text
        .chars()
        .filter(|&a| a != '\n')
        .map(|a| if a == '#' { 1 } else { 0 })
        .collect_vec();
    let image = image_text
        .split("\n")
        .filter(|a| a.len() > 0)
        .map(|line| line.chars().filter(|&a| a != '\n').map(|a| if a == '#' { 1 } else { 0 }).collect())
        .collect();

    let (image, infinity) = algo_step(&image, 0, &algo);
    let (end_image, _) = algo_step(&image, infinity, &algo);

    let result = end_image
        .into_iter()
        .flat_map(|a| a.into_iter())
        .filter(|&a| a == 1)
        .count();

    println!("Result: {}", result);
}

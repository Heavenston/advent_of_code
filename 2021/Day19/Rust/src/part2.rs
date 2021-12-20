use std::fs;
use arrayvec::ArrayVec;
use itertools::{ Itertools, iproduct };
use std::collections::{ HashMap, HashSet };
use nalgebra as na;

/*
fn vop2(a: &Vect3, b: &Vect3, op: impl FnMut(i32, (i32, i32)) -> i32) -> Vect3 {
    [op(0, (a[0], b[0])), op(1, (a[1], b[1])), op(2, (a[2], b[2]))]
}
*/

#[derive(Debug, Clone)]
struct Scanner {
    pub beacons: Vec<na::Vector4<i32>>,
    pub relative_map: HashMap<usize, na::Matrix4<f32>>,
}

fn get_relative_pos(scanner1: &Scanner, scanner2: &Scanner) -> Option<na::Matrix4<f32>> {
    let angles = (0..360).step_by(90);
    let rotations = iproduct!(angles.clone(), angles.clone(), angles.clone()).collect_vec();

    let mut diff_map = HashMap::new();
    let mut final_transform = None;

    'top_loop: for (xrot, yrot, zrot) in rotations {
        diff_map.clear();

        let t = na::geometry::Rotation3::from_euler_angles(
            (xrot as f32 / 180.) * std::f32::consts::PI,
            (yrot as f32 / 180.) * std::f32::consts::PI,
            (zrot as f32 / 180.) * std::f32::consts::PI,
        ).to_homogeneous();

        let diffs = scanner1.beacons.iter().map(|a| a.map(|a| a as f32))
            .cartesian_product(scanner2.beacons.iter().map(|a| a.map(|a| a as f32)))
            .map(|(b1, b2)| {
                b1 - (t * b2)
            })
            .map(|a| a.map(|b| b.round() as i32));

        for diff in diffs {
            match diff_map.get_mut(&diff) {
                None => { diff_map.insert(diff, 1); },
                Some(a) => {
                    *a += 1;
                    if *a >= 12 {
                        final_transform = Some(
                            t.append_translation(&diff.fixed_resize::<3, 1>(0).map(|a| a as f32))
                        );
                        break 'top_loop;
                    }
                },
            }
        }
    }

    return final_transform;
}

fn main() {
    let contents = fs::read_to_string("../input.txt").unwrap();

    let mut scanners = contents
        .split("\n\n")
        .map(|text| {
            let beacons = text
                .split("\n").skip(1)
                .filter(|g| g.len() > 0)
                .map(|a| a
                     .splitn(3, ",")
                     .map(|a| a.parse().unwrap())
                     .collect::<ArrayVec<i32, 3>>()
                )
                .map(|a| na::Vector4::new(a[0], a[1], a[2], 1))
                .collect_vec();

            Scanner {
                beacons,
                relative_map: HashMap::default(),
            }
        })
        .collect::<Vec<_>>();
    
    let mut done = HashSet::new();
    (0..scanners.len())
        .cartesian_product(0..scanners.len())
        .for_each(|(i, j)| {
            if i == j { return }
            if done.contains(&(i, j)) { return }
            done.insert((i, j));
            done.insert((j, i));

            println!("{} vs {}", i, j);
            let result = get_relative_pos(&scanners[i], &scanners[j]);
            if let Some(trs) = result {
                println!("-> {:?}", trs);
                scanners[j].relative_map.insert(i, trs);
                scanners[i].relative_map.insert(j, trs.try_inverse().unwrap());
            }
        });

    let mut global_map = HashMap::<usize, na::Matrix4<f32>>::new();
    global_map.insert(0, na::Matrix4::identity());

    let mut all_positions: Vec<na::Vector3<i32>> = Vec::new();

    // Calculate globals
    loop {
        let mut done_something = false;

        for (i, s) in scanners.iter().enumerate() {
            if global_map.contains_key(&i) { continue }
            let gkey = s.relative_map
                .keys()
                .filter(|k| global_map.contains_key(k))
                .next();
            if let Some(gkey) = gkey {
                let absolute = global_map[&gkey];
                let relative = s.relative_map[&gkey];
                let rs = absolute * relative;
                println!("{}[{}] -> {} {} {}", i, gkey, rs[12], rs[13], rs[14]);
                all_positions.push(na::Vector3::new(rs[12], rs[13], rs[14]).map(|a| a.round() as i32));
                global_map.insert(i, rs);
                done_something = true;
            }
        }

        if !done_something { break }
    }

    let m = all_positions
        .iter()
        .cartesian_product(all_positions.iter())
        .map(|(a, b)| a - b)
        .map(|a| a[0] + a[1] + a[2])
        .max();
    println!("Result: {:?}", m);

}

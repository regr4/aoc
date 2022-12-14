use std::collections::HashSet;

static INPUT: &str = include_str!("../input");

type Coordinate = (i64, i64);
type Board = HashSet<Coordinate>;

#[derive(Debug)]
struct Line {
    corners: Vec<Coordinate>,
}

fn parse_line(line: &str) -> Line {
    let mut res = Line { corners: vec![] };

    for c in line.split(" -> ") {
        let [x, y] = c.split(',')
	    .map(|x| x.parse().unwrap())
	    .collect::<Vec<_>>()[..]
	else {panic!("invalid line")};
        res.corners.push((x, y))
    }

    res
}

fn initialize_board() -> (Board, i64) {
    let mut board: Board = HashSet::new();
    let mut max_y = 0;

    let lines = INPUT.split('\n').filter(|l| !l.is_empty()).map(parse_line);

    for line in lines {
        for wi in line.corners.windows(2) {
            let [(x, y), (z, w)] = wi else {unreachable!("impossible")};

            max_y = max_y.max(*y).max(*w);

            if x == z {
                for val in *y.min(w)..=*y.max(w) {
                    board.insert((*x, val));
                }
            } else if y == w {
                for val in *x.min(z)..=*x.max(z) {
                    board.insert((val, *y));
                }
            }
        }
    }

    (board, max_y)
}

fn drop_sand(board: &mut Board, max_y: i64) -> bool {
    let (mut sand_x, mut sand_y) = (500, 0);

    loop {
        if sand_y > max_y || board.contains(&(sand_x, sand_y)) {
            // in the abyss or source blocked
            return true; // done
        }

        if !board.contains(&(sand_x, sand_y + 1)) {
            // go down
            sand_y += 1;
        } else if !board.contains(&(sand_x - 1, sand_y + 1)) {
            // go down and left
            sand_x -= 1;
            sand_y += 1;
        } else if !board.contains(&(sand_x + 1, sand_y + 1)) {
            // go down and right
            sand_x += 1;
            sand_y += 1;
        } else {
            // stuck but no abyss, so land
            board.insert((sand_x, sand_y));
            return false; // not done yet
        }
    }
}

fn main() {
    // part 1
    let (mut board, max_y) = initialize_board();
    let mut dropped_sand = 0;
    while !drop_sand(&mut board, max_y) {
        dropped_sand += 1;
    }
    println!("part 1: {dropped_sand}");

    // Could probably reuse the board but I don't care about performance
    // it runs in 0.3 s in release mode, which is good enough

    // part 2
    let (mut board, max_y) = initialize_board();
    println!("{max_y}");
    for x in 0..=1000 {
        // should be enough
        board.insert((x, max_y + 2));
    }
    let mut dropped_sand = 0;
    while !drop_sand(&mut board, max_y + 3) {
        dropped_sand += 1;
    }
    println!("part 2: {dropped_sand}")
}

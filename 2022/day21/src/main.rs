use std::collections::HashMap;
use std::collections::VecDeque;

static INPUT: &str = include_str!("../input");

type Label = String;

#[derive(Clone, Debug)]
enum Equation {
    Number(i64),
    Plus(Label, Label),
    Minus(Label, Label),
    Times(Label, Label),
    Divide(Label, Label),
}

#[derive(Clone, Debug)]
struct Monkey {
    name: String,
    value: Equation,
}

fn parse_monkey(s: &str) -> Monkey {
    let Some((name, rest)) = s.split_once(':')
    else {panic!()};

    let rest = rest.trim();

    if let Ok(n) = rest.parse::<i64>() {
        return Monkey {
            name: name.to_owned(),
            value: Equation::Number(n),
        };
    }

    let [p1, p2, p3] = rest.split_whitespace().collect::<Vec<_>>()[..]
    else {panic!()};

    let p1 = p1.to_owned();
    let p3 = p3.to_owned();
    let value = match p2 {
        "+" => Equation::Plus(p1, p3),
        "-" => Equation::Minus(p1, p3),
        "*" => Equation::Times(p1, p3),
        "/" => Equation::Divide(p1, p3),
        _ => panic!(),
    };

    Monkey {
        name: name.to_owned(),
        value,
    }
}

fn main() {
    let monkeys = INPUT.lines().map(parse_monkey).collect::<Vec<_>>();
    // for m in &monkeys {
    // println!("{m:?}");
    // }

    let mut monkey_map = HashMap::new();

    for m in &monkeys {
        monkey_map.insert(&m.name, m.value.clone());
    }

    // println!("{monkey_map:?}")
    let mut val_map: HashMap<&str, i64> = HashMap::new();

    for (k, v) in monkey_map.iter() {
        match v {
            Equation::Number(n) => {
                val_map.insert(k, *n);
            }
            Equation::Plus(_, _) => todo!(),
            Equation::Minus(_, _) => todo!(),
            Equation::Times(_, _) => todo!(),
            Equation::Divide(_, _) => todo!(),
        }
    }

    // let mut dq = VecDeque::from(monkeys);

    // println!("{inp_lines:?}");
}

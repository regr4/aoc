use regex::Regex;
use std::collections::HashMap;

static INPUT: &str = include_str!("../input");

// static INPUT: &str = r"Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
// Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.";

#[derive(Debug, PartialEq, Eq, Hash)]
struct Configuration {
    ore: i64,
    clay: i64,
    obsidian: i64,
    geodes: i64,

    ore_robots: i64,
    clay_robots: i64,
    obsidian_robots: i64,
    geode_robots: i64,

    time_left: i64,
}

impl Default for Configuration {
    fn default() -> Self {
        Self {
            ore: 0,
            clay: 0,
            obsidian: 0,
            geodes: 0,
            ore_robots: 1,
            clay_robots: 0,
            obsidian_robots: 0,
            geode_robots: 0,
            time_left: 24,
        }
    }
}

impl Configuration {
    // fn new(ore: i64, clay: i64, obsidian: i64, geodes: i64, time_left: i64) -> Self {
    //     Self {
    //         ore,
    //         clay,
    //         obsidian,
    //         geodes,
    //         time_left,
    //     }
    // }
}

#[derive(Debug)]
struct Blueprint {
    number: i64,
    ore_cost_ore: i64,
    clay_cost_ore: i64,
    obsidian_cost_ore: i64,
    obsidian_cost_clay: i64,
    geode_cost_ore: i64,
    geode_cost_obsidian: i64,
    cache: HashMap<Configuration, i64>,
}

impl Blueprint {
    fn new(
        number: i64,
        ore_cost_ore: i64,
        clay_cost_ore: i64,
        obsidian_cost_ore: i64,
        obsidian_cost_clay: i64,
        geode_cost_ore: i64,
        geode_cost_obsidian: i64,
    ) -> Self {
        Self {
            number,
            ore_cost_ore,
            clay_cost_ore,
            obsidian_cost_ore,
            obsidian_cost_clay,
            geode_cost_ore,
            geode_cost_obsidian,
            cache: HashMap::new(),
        }
    }

    fn from_line(line: &str) -> Self {
        let num = Regex::new(r"\d+").unwrap();

        let numbers = num
            .captures_iter(line)
            .map(|c| c[0].parse::<i64>().unwrap())
            .collect::<Vec<_>>();
        let [n, oco, cco, oco2, occ, gco, gcc] = numbers[..] else {
	    panic!("oh no");
	};
        Blueprint::new(n, oco, cco, oco2, occ, gco, gcc)
    }

    fn maximum_possible(
        &mut self,
        Configuration {
            ore,
            clay,
            obsidian,
            geodes,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
            time_left,
        }: Configuration,
        depth: i64,
    ) -> i64 {
        if time_left == 0 {
            return geodes;
        }

        if let Some(&r) = self.cache.get(&Configuration {
            ore,
            clay,
            obsidian,
            geodes: 0,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots: 0,
            time_left,
        }) {
            return r + time_left * geode_robots + geodes;
        }

        let mut best_possible = 0;

        if ore >= self.ore_cost_ore {
            best_possible = best_possible.max(self.maximum_possible(
                Configuration {
                    ore: ore - self.ore_cost_ore + ore_robots,
                    clay: clay + clay_robots,
                    obsidian: obsidian + obsidian_robots,
                    geodes: geodes + geode_robots,
                    ore_robots: ore_robots + 1,
                    clay_robots,
                    obsidian_robots,
                    geode_robots,
                    time_left: time_left - 1,
                },
                depth + 1,
            ))
        }

        if ore >= self.clay_cost_ore {
            best_possible = best_possible.max(self.maximum_possible(
                Configuration {
                    ore: ore - self.clay_cost_ore + ore_robots,
                    clay: clay + clay_robots,
                    obsidian: obsidian + obsidian_robots,
                    geodes: geodes + geode_robots,
                    ore_robots,
                    clay_robots: clay_robots + 1,
                    obsidian_robots,
                    geode_robots,
                    time_left: time_left - 1,
                },
                depth + 1,
            ))
        }

        if ore >= self.obsidian_cost_ore && clay >= self.obsidian_cost_clay {
            best_possible = best_possible.max(self.maximum_possible(
                Configuration {
                    ore: ore - self.obsidian_cost_ore + ore_robots,
                    clay: clay - self.obsidian_cost_clay + clay_robots,
                    obsidian: obsidian + obsidian_robots,
                    geodes: geodes + geode_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots: obsidian_robots + 1,
                    geode_robots,
                    time_left: time_left - 1,
                },
                depth + 1,
            ))
        }

        if ore >= self.geode_cost_ore && obsidian >= self.geode_cost_obsidian {
            best_possible = best_possible.max(self.maximum_possible(
                Configuration {
                    ore: ore - self.geode_cost_ore + ore_robots,
                    clay: clay + clay_robots,
                    obsidian: obsidian - self.geode_cost_obsidian + obsidian_robots,
                    geodes: geodes + geode_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots,
                    geode_robots: geode_robots + 1,
                    time_left: time_left - 1,
                },
                depth + 1,
            ))
        }

        best_possible = best_possible.max(self.maximum_possible(
            Configuration {
                ore: ore + ore_robots,
                clay: clay + clay_robots,
                obsidian: obsidian + obsidian_robots,
                geodes: geodes + geode_robots,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots,
                time_left: time_left - 1,
            },
            depth + 1,
        ));

        self.cache.insert(
            Configuration {
                ore,
                clay,
                obsidian,
                geodes: 0,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots: 0,
                time_left,
            },
            best_possible - geodes - time_left * geode_robots,
        );

        best_possible
    }

    fn quality_level(&mut self) -> i64 {
        println!("{}", self.number);
        let res = self.maximum_possible(Configuration::default(), 0);
        // println!("{}: {}", self.number, res);
        self.cache = HashMap::new(); // hopefully doesn't waste as much memory
        self.number * res
    }
}

fn main() {
    let mut blueprints = INPUT.lines().map(Blueprint::from_line).collect::<Vec<_>>();

    println!(
        "Part 1: {}",
        blueprints
            .iter_mut()
            .map(Blueprint::quality_level)
            .sum::<i64>()
    );

    // let mut blueprints = INPUT
    //     .lines()
    //     .take(3)
    //     .map(Blueprint::from_line)
    //     .collect::<Vec<_>>();

    // println!(
    //     "{}",
    //     blueprints
    //         .iter_mut()
    //         .map(|bp| {
    //             bp.maximum_possible(
    //                 Configuration {
    //                     time_left: 32,
    //                     ..Configuration::default()
    //                 },
    //                 0,
    //             )
    //         })
    //         .product::<i64>()
    // );

    // println!(
    //     "{}",
    //     (Blueprint {
    //         number: 1,
    //         ore_cost_ore: 4,
    //         clay_cost_ore: 2,
    //         obsidian_cost_ore: 3,
    //         obsidian_cost_clay: 14,
    //         geode_cost_ore: 2,
    //         geode_cost_obsidian: 7,
    //         cache: HashMap::new(),
    //     })
    //     .maximum_possible(
    //         Configuration::default(),
    //         // Configuration {
    //         //     ore: 4,
    //         //     clay: 25,
    //         //     obsidian: 7,
    //         //     geodes: 2,
    //         //     ore_robots: 1,
    //         //     clay_robots: 4,
    //         //     obsidian_robots: 2,
    //         //     geode_robots: 1,
    //         //     time_left: 4,
    //         // },
    //         0
    //     )
    // );
}

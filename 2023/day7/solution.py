"""day n"""

# common imports
from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from functools import total_ordering
import itertools
import re
from typing import Optional

with open("input") as f:
    inp = f.read().splitlines()


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@total_ordering
@dataclass
class Hand:
    cards: list[int]
    type: Optional[HandType]

    @staticmethod
    def from_code(s: str) -> "Hand":
        CARD_LOOKUP = {
            "*": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        cards = [CARD_LOOKUP[c] for c in s]
        return Hand(cards, None)

    def get_type(self) -> HandType:
        if self.type:
            return self.type

        jokers = self.cards.count(1)
        typ = HandType.HIGH_CARD

        # time for some bruteforcing
        for l in itertools.product(*[range(2, 15)] * jokers):
            replaced_cards = self.cards[:]
            c = 0
            for i in range(5):
                if replaced_cards[i] == 1:
                    replaced_cards[i] = l[c]
                    c += 1

            ctr = Counter(replaced_cards)

            match sorted(ctr.values()):
                case [5]:
                    t = HandType.FIVE_OF_A_KIND
                case [1, 4]:
                    t = HandType.FOUR_OF_A_KIND
                case [2, 3]:
                    t = HandType.FULL_HOUSE
                case [1, 1, 3]:
                    t = HandType.THREE_OF_A_KIND
                case [1, 2, 2]:
                    t = HandType.TWO_PAIR
                case [1, 1, 1, 2]:
                    t = HandType.ONE_PAIR
                case [1, 1, 1, 1, 1]:
                    t = HandType.HIGH_CARD

            typ = max(typ, t)

        self.type = typ
        return typ

    def __eq__(self, other) -> bool:
        return self.cards == other.cards

    def __lt__(self, other) -> bool:
        if self.get_type() < other.get_type():
            return True
        if self.get_type() > other.get_type():
            return False

        return self.cards < other.cards


# part 1
cards = []
for line in inp:
    [hand, bid] = line.split()
    cards.append((Hand.from_code(hand), int(bid)))
cards.sort()
res = sum(rank * bid for rank, (hand, bid) in enumerate(cards, start=1))
print(f"part 1: {res}")

# part 2
cards = []
for line in inp:
    [hand, bid] = line.split()
    cards.append((Hand.from_code(hand.replace("J", "*")), int(bid)))
cards.sort()
res = sum(rank * bid for rank, (hand, bid) in enumerate(cards, start=1))
print(f"part 2: {res}")

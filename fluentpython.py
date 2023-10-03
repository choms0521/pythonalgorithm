import collections
from math import hypot


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split(" ")

    def __init__(self):
        self.__cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool(abs(self))

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


my_vec_1 = Vector(5, 10)
my_vec_2 = Vector(1, 1)

print(my_vec_1 + my_vec_2)
print(my_vec_1 * 100)

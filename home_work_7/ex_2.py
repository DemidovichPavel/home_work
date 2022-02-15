from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def rag(self):
        pass

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def rag(self):
        return 2 * self.h + 0.3


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def rag(self):
        return self.v / 6.5 + 0.5

my_coat = Coat(10)
my_suit = Suit(1.86)
print(my_coat.rag)
print(my_suit.rag)
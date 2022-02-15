class Cage:
    def __init__(self, part):
        self.part = part

    def __add__(self, other):
        return Cage(self.part + other.part)

    def __sub__(self, other):
        a = self.part - other.part
        if a <= 0:
            print('nope')
        else:
            return Cage(a)

    def __mul__(self, other):
        return Cage(self.part * other.part)

    def __truediv__(self, other):
        return Cage(self.part // other.part)

    def make_order (self, count):
        my_str = ''
        for i in range(self.part // count):
            my_str += '*' * count + '\n'
        my_str += '*' * (self.part % count) + '\n'
        return my_str
    def __str__(self):
        return f'{self.part}'


my_cage_1 = Cage(10)
my_cage_2 = Cage(50)
print(my_cage_1.make_order(12))
print(my_cage_2.make_order(13))
print(my_cage_1 - my_cage_2)
print(my_cage_1 + my_cage_2)
print(my_cage_1 * my_cage_2)
print(my_cage_1 / my_cage_2)
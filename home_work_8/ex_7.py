class Numbers:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Numbers(self.number_1 + other.part)

    def __mul__(self, other):
        return Numbers(self.part * other.part)

my_numbers_1 = (52)
my_numbers_2 = (18)
print(my_numbers_1 + my_numbers_2)
print(my_numbers_1 * my_numbers_2)
from random import randint

class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        my_str = ' '
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                my_str += f'{self.numbers[i][j]:3} '
            my_str += '\n'
        my_str +=  '\n'


        return my_str

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.numbers)):
            new_str = []
            for j in range(len(self.numbers[i])):
                sum_mat = self.numbers[i][j] + other.numbers[i][j]
                new_str.append(sum_mat)
            new_matrix.append(new_str)
        return Matrix(new_matrix)

matrix_1 = Matrix([[randint(-10, 10) for i in range(5)] for j in range(5)])
matrix_2 = Matrix([[randint(-10, 10) for i in range(5)] for j in range(5)])
print(matrix_2)
print(matrix_1)
print(matrix_2 + matrix_1)
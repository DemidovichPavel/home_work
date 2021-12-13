def num_degree(arg_1, arg_2):
    c = arg_1 ** arg_2
    return c
user_number = int(input('Введите целое положительное число '))
user_degree = int(input('Введите отрицательное число степень '))
print(num_degree(user_number, user_degree))





degree = lambda num_1, num_2: num_1 ** num_2

num_1 = int(input('Введите целое положительное число '))
num_2 = int(input('Введите отрицательное число степень '))
print(degree(num_1, num_2))



def num_degree(x, y):
    n = abs(y)
    z = x
    while n != 1:
        x = x * z
        n = n - 1
    if y < 0:
        x = 1 / x
    return x

user_number = int(input('Введите целое положительное число '))
user_degree = int(input('Введите отрицательное число степень '))
print(num_degree(user_number, user_degree))



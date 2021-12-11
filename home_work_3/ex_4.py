def num_degree(arg_1, arg_2):
    c = arg_1 ** arg_2
    return c
user_number = int(input('Введите целое положительное число '))
user_degree = int(input('Введите отрицательное число степень '))
print(num_degree(user_number, user_degree))





def num_degree(x, y):
    n = abs(y)
    z = x
    while n != 1:
        x = z * x
        n = n - 1
    if y < 0:
        x = 1 / x
    return x

user_number = int(input('Введите целое положительное число '))
user_degree = int(input('Введите отрицательное число степень '))
print(num_degree(user_number, user_degree))



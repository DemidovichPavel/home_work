def sum_numbers(arg_1, arg_2, arg_3):
    c = sum((arg_1, arg_2, arg_3)) - min(arg_1, arg_2, arg_3)
    return c


users_numbers_1 = int(input('Введите первое число '))
users_numbers_2 = int(input('Введите второе число '))
users_numbers_3 = int(input('Введите третье число '))
a = sum_numbers(users_numbers_1, users_numbers_2, users_numbers_3)
print(a)

# def sum_numbers(numbers):
#     a = numbers[-1]
#     b = numbers[-2]
#     c = a + b
#     return c
# user_number = input('Введи числа ').split()
# my_list = map(int, user_number)
# my_list_2 = sorted(my_list)
# print(sum_numbers(my_list_2))

# По-моему вариант более уневерсальный. Это на тот случай, когда пользователь ввел более трех чисел






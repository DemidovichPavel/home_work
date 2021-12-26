def sum_numbers(arg_1, arg_2):
        if arg_2 == 0:
            print('На ноль делить нельзя!!!')
        else:
             resalt = arg_1 / arg_2
             return resalt

user_numerate = int(input('Введите числитель: '))
user_denominator = int(input('Введите знаменатель: '))
print(sum_numbers(user_numerate, user_denominator))


# def del_numbers(numbers):
#     if int(numbers[1]) == 0:
#         print('Нельзя делить на ноль!!! ')
#     else:
#         total = int(numbers[0]) / int(numbers[1])
#         return total
# users_number = input('Давай введем два значения: ').split()
# print(del_numbers(users_number))







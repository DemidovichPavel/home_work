# import time as t
# from time import sleep as sl
#
#
#
#
# print('hello')
# sl(5)
# print('world')



# from sys import argv
#
#
#
# print(argv)
#
# n_1 = int(argv[1])
# n_2 = int(argv[2])
# print(n_2 * n_1)

#my_list = [i / 7 for i in range(12) if i % 1 == 0]
# print(my_list)
# my_dict = {}
# for i in range(12):
#     if i % 2 == 0:
#         my_dict[str(i)] = i
#
#
# my_dict_2 = {str(i) : i for i in range(12) if i % 2 == 0}
#
print(my_list)
# print(my_dict_2)

from random import randint, randrange, random

#resalt = randint(1, 100)
#resalt = randrange(0, 10, 2)
# resalt = random() * 10
#print(resalt)


#
# user_input = int(input('write a number: '))
#
# def fact_numbers (user_number):
#     fact = 1
#     for i in range(1, user_number + 1):
#         fact *= i
#         yield fact
#
# for element in fact_numbers(user_input):
#     print(element)



from itertools import count, cycle

# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# my_cycle = cycle(my_list)
# for i in range(7):
#     print(next(my_cycle))



my_counter = count(5)
for i in range(10):
    print(next(my_counter))




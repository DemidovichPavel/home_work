from itertools import count, cycle


# my_counter = count(3)
# for i in range(15):
#     print(next(my_counter))

my_list = ['Today', 'is', 'a', 'good', 'day', ' in', 'order', 'to', 'walk']
my_sycle = cycle(my_list)
for i in range(15):
    print(next(my_sycle))


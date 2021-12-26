from functools import reduce

def sum_numbers(a, b):
    return a + b


my_list = [i for i in range(100, 1001) if i % 2 == 0]
result = reduce(sum_numbers, my_list)
print(result)

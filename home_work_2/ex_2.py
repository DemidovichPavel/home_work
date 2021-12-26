numbers = input('Введите числа разделенные пробелом ')
my_list = numbers.split()
my_list_2 = len(my_list)
i = 0

while my_list_2 - 1 > i:
    my_list[i], my_list[i+1]  = my_list[i+1],  my_list[i]
    i = i + 2
print(my_list)









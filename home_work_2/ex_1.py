
my_list = [1, 2, 5, 5, 54, 'good', 'mother', False]
total = len(my_list)
while total > 0:
    ind = my_list[0]
    print(ind)
    print(type(ind))
    my_list.pop(0)
    total = total - 1



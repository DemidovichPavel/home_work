stop = False
my_sum = 0
while not stop:
    user_list = input('Введите данные ').split()
    for i in user_list:
        if i == 'stop':
            stop = True
            break
        else:
            my_sum += int(i)
    print(my_sum)





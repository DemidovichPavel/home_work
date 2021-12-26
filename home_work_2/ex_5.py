my_list = [7, 5, 2, 1, 0]
user_number = int(input('какое число напишем дальше? '))
c = False # эту строку списал с Вашего разбора. Без нее работал код, но не коректно
for i, n in enumerate(my_list):
    if user_number > n:
        my_list.insert(i, user_number)
        c = True
        break
if not c:
    my_list.append(user_number)
print(my_list)







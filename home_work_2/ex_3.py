seasons = {'Зима':(12, 1, 2),'Весна':(3, 4, 5),'Лето':(6, 7, 8),'Осень':(9, 10, 11)}
user_mouth = int(input('Какой ммесяц выберем? '))
if user_mouth > 12 or user_mouth < 0:
    print('Пора бы знать количество месяцев')
else:
    for key in seasons.keys():
        if user_mouth in seasons[key]:
            print(key)


user_mouth_2 = int(input('Еще разок запили месяц '))
a = 'winter'
b = 'spring'
c = 'summer'
d = 'automn'

my_list = [a, a, b, b, b, c, c, c, d, d, d, a]
print(my_list[int(user_mouth_2) - 1])











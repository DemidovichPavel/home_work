distance_1 = int(input('Введи пройденое расстояние в первый день '))
distance_2 = int(input('Введи расстояние, которое ты планируешь пройти '))
percent = int(input('Введи процент, на который будешь увеличивать пройденое расстояние '))
percent = percent / 100
day = 1
if distance_1 > distance_2:
    print('Ты деградируешь')
elif distance_1 == distance_2:
    print('Ты топчишься на одном месте')
else:
    while distance_1 < distance_2:
        print(f' {day} день : {distance_1}')
        distance_1 = distance_1 + (distance_1 * percent)
        day += 1
    print(f' {day} день : {distance_1}')
    print(f'на {day} ты пройдешь {distance_1}')








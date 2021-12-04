sentence = input('что запищем? ')
a = sentence.split()
n = 1
for i in a:
    print(f'{n}  {i[:10]}')
    n+=1
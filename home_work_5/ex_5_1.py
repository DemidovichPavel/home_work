import random

with open('ex_5.txt', 'w') as file:
    for i in range(100):
        file.write(f'{random.randrange(0, 50, 4)} ')

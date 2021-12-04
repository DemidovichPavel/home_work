a = int(input('введи число '))
b = a % 10
while a > 0:
    a = a // 10
    if b < a % 10:
        b = a % 10
print(b)




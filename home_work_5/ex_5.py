with open('ex_5.txt') as file:
    our_numbers = file.read().split()
    sum = 0
    for i in our_numbers:
        sum += int(i)
    print(sum)
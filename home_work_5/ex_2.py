with open('ex_2.txt') as file:
    my_file = file.readlines()
    count = 0
    for i, word in enumerate(my_file):
        count += 1
        words = len(word.split())
        print(f'{count} - {words}')
    print(count)


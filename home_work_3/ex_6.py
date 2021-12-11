def shift_text(my_str):
    n = ''
    for i in my_str:
        c = i[0].upper() + i[1:]
        n += ' ' + c
    return n


user_text = input('Что звпишем? ').split()
print(shift_text(user_text))


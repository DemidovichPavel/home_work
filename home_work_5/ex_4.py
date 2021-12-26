my_dict = {
    'One':"Один",
    'Two':"Два",
    'Three':"Три",
    'Four':"Четыри"
}

with open('ex_4.txt') as file, open('new_file.txt', 'w') as new_file:# В разборах не было рассказано, что можно сразу открывать фаил на чтание и на запись
    my_list = file.readlines()
    for i in my_list:
        new_list = i.split()
        ch_numbers = my_dict.get(new_list[0])
        new_file.write(f'{i.replace(new_list[0], ch_numbers)}')

    # Я не пойму где ошибка!!!!!
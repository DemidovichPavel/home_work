with open ('test.txt', 'w') as file:
    file.write('Hey, Bedrenka! How are you?\n')
    file.write('Have you got up yet?')
    string=['Why did not you phone me?\n I am waiting you phone. ']
    file.writelines(string)
    my_str = 'Why did not you phone me?\n I am waiting you phone. '
    my_str_2 = 'We are gonna meet today?'
    print(my_str, file=file)
    print(my_str_2,file=file)


#
# with open ('test_2.txt', 'x') as file:
#     file.write('Could we meet at the center city?')
#
#
# with open ('test_3.txt', 'a') as file:
#     my_str = ['Could we meet at the center city?\n']
#     file.writelines(my_str)
#     my_str_2 = ['Ok, i will wait you there\n we will at 5 o clock ']
#     file.writelines(my_str_2)
#
# with open ('test.txt') as file:
#     # content = file.read()
#     content = file.readline()
#     resalt = f"fife contains this text'{content}'"
#     print(resalt)
#     content = file.readline()
#     resalt = f"fife contains this text'{content}'"
#     print(resalt)
#
# with open('test.txt') as file:
#     #content = file.readlines()
#     for i in file:
#         print(i, end='')
# with open('test.txt') as file:
#     print(file.tell())
#     content = file.readlines()
#     print(file.tell())
#     file.seek(3)
#     content_1 = file.readlines()
#     print(content)
#     print(content_1)

#
# with open('test.txt') as file:
#     st_b = []
#     temp = 'asd'
#     while temp:
#         st_b.append(file.tell())
#         temp = file.readline()
#     print(st_b)
#     file.seek(27)
#     print(file.readline())
#
# import os
# # os.remove('test_3.txt')
# os.rename('test.txt', 'new_test.txt')
#
import json


# # Одно из заданий ДЗ
# with open('test_j.json') as file:
#     result = file.read()
#     print(result)
#     print(type(result))
#     my_str = json.loads(result)
#     print(my_str)
#     print(type(my_str))
#     for key, value in my_str.items():
#         print(f'{key} - {value}')
import json

# my_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
# }
# with open('test_j.txt', 'w') as file:
#     j_str = json.dumps(my_dict)
#     print(j_str)
#     print(type(j_str))
#     file.write(j_str)




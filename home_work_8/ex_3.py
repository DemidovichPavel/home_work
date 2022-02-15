class My_Exeption(Exception):

    def __init__(self, numbers):
        self.numbers = numbers


my_list = []
stop = False

while not stop:
    try:
        user_input = input('wrire a symbol ')
        if user_input == 'stop':
            break
        if int(user_input):
            my_list.append(user_input)
        print(my_list)
    except:
        print('The variable is not a number')














#     while stop_word = False:
#     user_number_1 = input('write whatever')
#     if user_number_1
#     user_number_2 = int(input('write second number '))
#     if user_number_2 == 0:
#         raise My_Exeption('must not to divide by 0')
#     else:
#         resalt = user_number_1 / user_number_2
#         print(resalt)
# except My_Exeption as i:
#     print(i)
# print('end of script')



#
# tmp = int(myVariable)
#     print('The variable a number')
# except:
#     print('The variable is not a number')
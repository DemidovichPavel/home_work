class My_Exeption(Exception):

    def __init__(self, numbers):
        self.numbers = numbers

try:
    user_number_1 = int(input('write first number '))
    user_number_2 = int(input('write second number '))
    if user_number_2 == 0:
        raise My_Exeption('must not to divide by 0')
    else:
        resalt = user_number_1 / user_number_2
        print(resalt)
except My_Exeption as i:
    print(i)
print('end of script')
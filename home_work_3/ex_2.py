def users_date(arg_1, arg_2, arg_3, arg_4, arg_5 ):
    total = 'Данные пользователя: ' + arg_1 +', '+ arg_2 +', '+ arg_3 +', '+ arg_4 +', '+ arg_5
    return total

name = input('Ваше имя ')
surname = input('Ваша фамилия ')
city = input('Где Вы проживаете ')
tel_number = input('Ваш номер телефона ')
email = input('Ваша электронная почта ')
print(users_date(arg_1 = name, arg_2 = surname, arg_3 = city,arg_4 = email,arg_5 = tel_number ))

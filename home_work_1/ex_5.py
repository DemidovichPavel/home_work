print('Давайте посчитаем рентабильность фирмы')
get_company = int(input('введите доход компании в рублях '))   # доход компании
give_company = int(input('введите траты компании в рублях '))   # расход компании

if get_company < give_company:
    print('Ваша компания убыточная')
elif  get_company == give_company:
    print('вы отработали в ноль')
elif get_company > give_company:
    result = get_company - give_company
    print('Чистая прибыль вашей комании = ' + str(result) + ' рублей' )
    print('Вы отлично поработали')
    #total = f'Чистая прибыль вашей компании =  {result}  рублей'    второй варианр реализации вывода информации
    #print(total)
    clerk = int(input('А сколько у Вас сотрудников?'))
    income_clerk = result / clerk
    print(str(income_clerk) + ' рублей дохода на каждого сотрудника')









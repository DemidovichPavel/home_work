with open('ex_3.txt') as file:
    clerk = file.readlines()
    clerks_company = {}
    total_salary = 0
    for i in clerk:
        clerks = i.split()
        clerks_company.update({clerks[0]: int(clerks[1])})
        total_salary += int(clerks[1])
    print(clerks_company)
    avar = total_salary / len(clerks_company)
    print(avar)
for key, value in clerks_company.items():
    if value < 20000:
        print(f'{key}: {value}') # Долго я не мог вывести ЗП менее 20000, подсмотрел у Вас решение. Оказывается я непоставил items)))

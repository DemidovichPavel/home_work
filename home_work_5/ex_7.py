import json

companies = {}
count = 0
sum = 0
with open('ex_7.txt') as file:
    our_companies = file.readlines()
    for i in our_companies:
        our_companies_sep = i.split()
        print(our_companies_sep)
        income = int(our_companies_sep[2]) - int(our_companies_sep[3])
        companies.update({our_companies_sep[0]: income})
        print(companies)
        if income < 0:
            count += 1
            sum = sum +income
ave_inc = sum / count
my_dict = [companies, {'': ave_inc}]
print(my_dict)
with open('ex_7.json', 'w') as file:
    json.dump(my_dict, file)



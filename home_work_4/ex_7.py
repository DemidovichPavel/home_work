
def fact_numbers (user_number):
    fact = 1
    for i in range(1, user_number + 1):
        fact *= i
        yield fact

user_input = int(input('write a number: '))
print(fact_numbers(user_input))
for element in fact_numbers(user_input):
    print(element)


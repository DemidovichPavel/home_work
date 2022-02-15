with open('test_ex_1', 'w') as file:
    user_text = input('What will you write? ')
    while user_text:
        file.write(f'{user_text}')
        user_text = input('What will you write? ')

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name}, {self.surname}, {self.position}'

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return f'total_income = {total_income}'


my_worker = Position('Ivan', 'Ivanov', 'builder', 45000, 37500)
print(my_worker.get_full_name())
print(my_worker.get_total_income())
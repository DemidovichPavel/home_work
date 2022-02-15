class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def drow(self):
        print(f'Сначала ручкой напишем {self.title}')


class Pencil(Stationery):
    def drow(self):
        print(f'Не, карандашом попробуем {self.title}')


class Handle(Stationery):
    def drow(self):
        print(f'Тоже не то. Может маркер? {self.title}')

my_stationary = Stationery('- в черновичок')

pen = Pen(my_stationary.title)
pencil = Pencil(my_stationary.title)
handle = Handle(my_stationary.title)
for i in (pen, pencil, handle):
    i.drow()
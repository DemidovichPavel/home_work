class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'{direction}')

    def show_speed(self):
        print(f'speed = {self.speed}')

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('you have to drive slow down')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('you have to drive slow down')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

tc = TownCar(70, 'yellow', 'Toyota')
sc = SportCar(100, 'red', 'Lombargini')
wc = WorkCar(70, 'white', 'Nissan')
pc = PoliceCar(70, 'blue', 'Skoda')

tc.show_speed()
wc.show_speed()
sc.turn('right')
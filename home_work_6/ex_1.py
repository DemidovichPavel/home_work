from time import sleep as sl

class Trafficlight:
    color = (('red',7), ('yellow', 2), ('green', 8))
    sec = (7, 2, 8)
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            for i in self.color:
                self.__color = i[0]
                print(self.__color)
                sl (i [1])


tr_li = Trafficlight('red')
tr_li.running()
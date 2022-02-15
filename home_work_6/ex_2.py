class Road:

    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def weght_stuff_of_road(self, asphalt, thick):
        wsor = self.__width * self.__lenght * asphalt * thick
        return f'{wsor} - kilo'

area = Road(1000, 12)
my_culc = area.weght_stuff_of_road(20, 7)
print(my_culc)

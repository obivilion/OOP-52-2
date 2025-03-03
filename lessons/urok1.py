from urllib.response import addinfourl


class Car:
    # конструктор класса
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def signal(self):
        print(f'{self.color} car signal')

    # метод класса
    def action(self):
        return print(f'{self.model} start action')
#обьект класса | экземпляр класса
mazda = Car('RX-8', 2004, 'Red')
BMW = Car('M-5 f90', 2023, 'Black')

mazda.action()
BMW.action()

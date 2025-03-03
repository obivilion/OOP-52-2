#Декопозиция проекта . Наследования Инкапсулятсия ООП GIT

#Наследования

#Родиелский класс / базовый класс / Супер класс
class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def introduce(self):
        return print(f'{self.name}, мой уровинь {self.lvl}')

    def action(self):
        return print(f'{self.name} выполняет базовое действие')

# CamelCase - Верблюжая натация - UpperCamelCase & lowerCAmelCase
#Дочерним классом
class Warrior(Hero):

    def __init__(self,name,lvl,hp,st):
        super().__init__(name, lvl, hp)
        self.st = st
    def attack(self):
        if self.st >= 10:
            return print(f'{self.name} атакует мечом!!')
        else:
            return print(f'{self.name} мало стомины!!')

Kirito = Warrior('Kirito', 100, 1000, 10)

# snake_case змеиеая нотация
Kirito.action()
Kirito.introduce()
Kirito.attack()
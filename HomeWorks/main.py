from abc import ABC, abstractmethod

from random import random

class Hero:

    def __init__(self, name, attack, protection, rest):
        self.name = name
        self.attack = attack
        self.protection = protection
        self.rest = rest
        self.__random_int = random



    def get_random_int(self):
        return random

    @abstractmethod
    def unique_attack(self):
        return print('Attack')

    @abstractmethod
    def unique_scream(self):
        return print('OYYYY')

    @abstractmethod
    def action(self, get_random_int):
        if get_random_int == 1:
            self.attack = get_random_int
        elif get_random_int == 2:
            self.protection = get_random_int

        else:
            return 3 == self.rest




Sam = Hero("name", 12, 200, 2)
Sam.get_random_int()


Sam.unique_attack()
Sam.unique_scream()
Sam.action(2)
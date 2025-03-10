from abc import ABC, abstractmethod
from logging import setLogRecordFactory
from math import radians

from random import randint

class Hero:

    def __init__(self, name, attack, protection, rest):
        self.name = name
        self.attack = attack
        self.protection = protection
        self.rest = rest
        self.__random_int = randint



    def get_random_int(self):
        return randint(1, 3)

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass





Sam = Hero("name", 12, 200, 2)
# Sam.action()


# Sam.unique_attack()
# Sam.unique_scream()
# Sam.action(2)
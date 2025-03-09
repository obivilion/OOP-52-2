# # Инкапусляция - Абстраксия
# # def some(self): - открытый метод
# # def _some(self): - закрытый метод
# # def __some(self): - приватный метод
#
# # self.some(self): - открытый атребут
# # self. _some(self): - закрытый атребут
# # self. __some(self): - приватный атребут


class BankAccount:

    def __init__(self, username, balance, pin_code):
        self.username = username
        self._balance = balance
        self.__pin_code = pin_code


    def deposit(self, amount):
        if amount > 0:
            self.__to_up_balance(amount)
            return print(f'Баланс {self.username} пополнен на {amount}. \n Текуший баланс {self._balance}')
        else:
            return print('Сумма должна быть положительной')

    def __to_up_balance(self,amount):
        self._balance += amount

    def get_balance(self, pin_code):
        if self.__pin_code == pin_code:
            return print(f'Ваш баланс: {self._balance}')
        else:
            return print('не верный пин-код')


user1 = BankAccount('Ardager', 1000, 1234)
# print(user1._balance)
# print(user1._BankAccount__pin_code)
user1.get_balance(1234)
user1.deposit(1000)


# #Абстракция

# from abc import ABC, abstractmethod
# from traceback import print_tb
#
#
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass #определеный интерфейс для звука
#
#     @abstractmethod
#     def move(self):
#         pass #определеный интерфейс для движения
#
# class Dog(Animal):
#
#     def make_sound(self):
#         return print('Gaf gaf')
#
#     def move(self):
#         return print('move')
#
# qufi = Dog()
# qufi.make_sound()
# qufi.move()
#
# class SmsServiceAbc(ABC):
#
#     @abstractmethod
#     def send_sms(self):
#         pass

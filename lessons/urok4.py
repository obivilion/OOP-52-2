# staticmethod (статический метод) — это метод, который не требует доступа к экземпляру или
# классу. Он ведет себя как обычная функция, но внутри класса.



class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

# print(MathUtils.add(1,4))



# classmethod (метод класса) — это метод, который получает доступ к самому классу, а не к его экземплярам.



class Person:

    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


    @classmethod
    def get_count(cls):
        return cls.count

    def test(self):
        pass


p1 = Person("Alice")
p2 = Person("John")
p3 = Person("Oleg")


# print(Person.get_count())


class Person:


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def test(self):
        return f"{self.first_name} {self.last_name}"


    @test.setter
    def test(self, value):
        first, last = value.split()
        self.first_name = first
        self.last_name = last



# p = Person("John", "Doe")
# print(p.test)
# p.test = "Ardager Dev"
# print(p.first_name)
# print(p.last_name)


# Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает
# измененную или новую функцию. Они позволяют добавлять новую функциональность к существующим
# функциям без изменения их кода.


# Пример простого декоратора

def my_decorator(func):   # 3

    def wrapper():   # %
        print("Перед выполнением функции") # 6
        func() # 7
        print('После выполнением функции') # 9

    return wrapper # 4


@my_decorator
def hello():               # 2
    print("Привет") # 8


# hello() # 1


# Декораторы с аргументами

def repead(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

t = int(input('Ведите количество: '))

@repead(t)
def greet():
    print('Hello')

greet()

# Декораторы для классов

def clss_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print('New method')
    return NewClass

@

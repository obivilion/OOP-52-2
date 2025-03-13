hello = 'Мой друг'.upper()
hi = 'Привет'.upper()
def uppercase(func):


    def wrapper():
        print(f'{hello}')
        func()

    return wrapper

@uppercase
def say_hello():
    return print(f'{hi}')

say_hello()

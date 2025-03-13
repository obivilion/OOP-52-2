def uppercase(func):

    hello = 'Мой друг'.upper()
    def wrapper():
        print(f'{hello}')
        func()

    return wrapper

@uppercase

def say_hello():
    hi = 'Привет'.upper()
    return print(f'{hi}')

print(say_hello())

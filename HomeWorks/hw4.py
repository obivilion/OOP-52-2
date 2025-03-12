def uppercase(func):

    def wrapper():
        print("Мой друг ")
        func()

    return wrapper

@uppercase
def say_hello():
    return print("Привет!")

say_hello()

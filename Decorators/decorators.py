# Decorators

# Everything in python is an Object
# that means functions can be used as objects

# a decorator takes a function, adds some functionality and returns it

#Basic Decorator
# in this example we will change the execution order
def test_decorator(func):
    print(f'before')
    func()
    print(f'after')

@test_decorator
def do_stuff():
    print(f'doing stuff')

print(f'-'*25)

#Real Decorator
# in this example we will change the functionality
def makeBold(func):
    def inner():
        print(f'<b>')
        func()
        print(f'</b>')
    return inner # returns the inner function

@makeBold
def printName():
    print('Bryan')

print(f'Calling here..')
printName()

print(f'-'*25)

#Decorator with Params
# this has a defined no. of params
def numCheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Cannot divide by Zero')
                return False
            return True
        print(f'{o} is not a number..')
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x,y)
    return inner

@numCheck
def divide(a,b):
    print(a/b)

divide(100, 3)
divide(100, 0)
divide(100, 'cat')

print(f'-'*25)

# Decorator Chaining
# Decorators with unknown number of params - *args and **kwargs
def outline(func):
    def inner(*args, **kwargs):
        print(f'~ '*20)
        func(*args, **kwargs)
        print(f'+ '*20)
    return inner

def listItems(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'arg = {x}')
        for k,v in kwargs.items():
            print(f'key = {k} and value = {v}')
    return inner

@outline
@listItems
def display(msg):
    print(msg)

display('Hello World')


@outline
@listItems
def birthday(name='', age=0):
    print(f'Happy Bday {name}, you are {age} years old!')

birthday(name='Bryan', age=16)

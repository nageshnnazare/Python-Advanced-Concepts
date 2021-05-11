#Map

# looping without a loop
# Map function calls to a collection of items

#Basic Usagee - count len
people = ['Matt', 'Bryan', 'Tammy', 'Markus']

#old way
counts = []
for x in people:
    counts.append(len(x))
print(f'Old Way: {counts}')

#Modern way
print(f'Mapped: {list(map(len,people))}')

#More Complex - Combine elemnts
#Notice differnt lens, we are also passing multiple args
first_names = ('Apple', 'Chocolate', 'Fudge', 'Pizza')
last_names = ('Pie', 'Cake', 'Brownies')

def merg(a,b):
    return a + ' ' + b

x = map(merg, first_names, last_names)
print(list(x))

#Multiple Functions in one Map call
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def doall(func,num):
    return func(num[0], num[1])

f = (add, subtract, multiply, divide)
v = [[5,3]]  
n = list(v) * len(f)
print(f'f:{f}, n:{n}')

m = map(doall,f, n)
print(f'Result: {list(m)}')
# Iterators
# Making counting easy

t = (1,2,3,4)
for x in t:
    print(x)

# Iter Basics:
# list, tuple, dictionary, and set are all iterable objects
# they are iterable objects which you can get an iterator from
people = ['Bryan', 'Tammy', 'Rango']
i =iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) # Stop Iteration

#Iterable Class
import random
class Lotto():
    def __init__(self):
        self._max = 5

    def __iter__(self):
        # the "yield" statement suspents the function's execution & 
        # sends a value back to the caller, but retains enough state
        # to enable function to resume where it is left off
        for _ in range(self._max):
            yield random.randrange(0, 100)

    def setMax(self,value):
        self._max = value

print(f'-'*25)
lotto = Lotto()
lotto.setMax(10)

for x in lotto:
    print(x)

print(f'-'*25)
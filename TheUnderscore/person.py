# Test Class:

class Person:
    # Weak private
    _name = 'No name'

    def setName(self, name):
        self._name = name
        print(f'Name set to {self._name}')

    # Strong private
    def __think(self):
        print(f'Thinking to myself')

    def work(self):
        self.__think()

    # Before and after
    def __init__(self):
        print(f'Constructor')

    def __call__(self):
        print(f'Call Someone')


class Child(Person):
    def testDouble(self):
        self.__think(self)

# The Cat class:

# self is the first parameter - equivalent to "this"

class Cat:
    name = ''
    age = 0
    color = ''

    def __init__(self, name, age=0, color='white'):
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructer for {self.name}')

    def meow(self):
        print(f'{self.name} says meow!!')

    def sleep(self):
        print(f'{self.name} says zzZ')

    def hungry(self):
        for x in range(5):
            self.meow()
            
    def eat(self):
        print(f'{self.name} says nom nom nom')

    def description(self):
        print(f'{self.name} is a {self.color} cat, who is {self.age} years old !!')

    
    
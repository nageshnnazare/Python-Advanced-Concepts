# Class Inheritance

# Feline Class
class Feline:
    def __init__(self, name):
        self.name = name
        print(f'Creating the Feline class')

    def setName(self, name):
        print(f'{self} setting name {name}')
        self.name = name 
        
    def meow(self):
        print(f'{self.name} says meow !')

# Lion Class
class Lion(Feline):
    def roar(self):
        print(f'{self.name} roars !')

# Tiger Class
class Tiger(Feline):
    # overiding the constructor is a bad idea!!
    def __init__(self):
        # super allows to access the parent 
        super().__init__('No Name')
        print(f'Creating the Tiger class')
    
    def stalk(self):
        # make sure the name is set in the parent
        # this is called Look Before you Leap
        # here we are dynamically adding the Attribute

        # if we did not init the super, we have to be careful
        print(f'{self.name} stalking')

    def rename(self, name):
        super().setName(name)


c = Feline('kitty')
print(c)
c.meow()

l = Lion('leo')
print(l)
l.meow()
l.roar()

t = Tiger() # is a feline with a different constructor
print(t)
t.stalk()
t.rename('Tony')
t.meow()
t.stalk()
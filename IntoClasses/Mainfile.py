#Introduction to class

from cat import Cat as Cat

# Using the class:
def test():
    b = Cat('Kit-kat', 2, 'tabby')
    c = Cat('Othello', 6, 'black')

    b.description()
    c.description()

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()


if __name__ == "__main__":
    x = Cat('test')
    print(x)
    test()

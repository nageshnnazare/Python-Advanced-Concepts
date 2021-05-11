#Pickle
#dill

#Serializing Objects
# Saving and loading objects and their states
# python datatypes and top level classes

import pickle

#Simple Decorator
def outline(func):
    def inner(*args, **kwargs):
        print(f'-'*25)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print(f'-'*25)
    return inner

#simple Class
class cat:
    def __init__(self, name, age, info):
        self.__name = name
        self.__age = age
        self.__info = info

    @outline
    def display(self, msg=''):
        print(msg)
        print(f'{self.__name} is {self.__age} year old cat')
        for k,v in self.__info.items():
            print(f'{k} = {v}')

othello = cat('Othello', 15, dict(color='Black',weight=15,loves='eating'))
othello.display('Testing')

#Serialize
sc = pickle.dumps(othello)
print(sc)

with open('cat.txt', 'wb') as f:
    pickle.dump(othello, f)

#Deserialize
mycat = pickle.loads(sc)
print(f'from string')
mycat.display('from string')

with open('cat.txt', 'rb') as f:
    diskcat = pickle.load(f)
diskcat.display('from disk')

print(mycat)
print(diskcat)
# The Underscores:

# _Single
# __Double
# __Before
# After__
# __Both__

# Skipping:
for _ in range(5):
    print(f'hello')

# Test class
from person import *

# _Before (Single)
# Internal use only -> called the weak private
p = Person()
p.setName('Bryan')
print(f'Weak private {p._name}')
p._name = 'NOOOO'
print(f'Weak private {p._name}')


# __Before (Double)
# Internal use only -> avoid conflict in subclass
# and tell the python to rewrite the name (Mangling)
p = Person()
p.work()
# p.__think()
c = Child()
# c.testDouble()


# After (Any)
# helps to avoid naming conflicts with the keywords
class_ = Person()
print(class_)


# Before and after
# considered special to python (like main and init functions)
p = Person()
p.__call__()



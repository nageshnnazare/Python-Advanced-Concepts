#Exceptions
# If bad things happen, we need to know how to handle it

"""
Errors mostly occur during the runtime, that is they belong to unchecked type.
Exceptions are the problems that can occur during the compile and runtime

Exceptions are divided into two categories:
Checked Exceptions and Unchecked Exceptions
"""

#Simple Decorator
def outline(func):
    def inner(*args, **kwargs):
        print(f'-'*25)
        print(f'Function: {func.__name__,}')
        func(*args, **kwargs)
        print(f'-'*25)

    return inner

#Try, Except and Finally
@outline
def test_one(x,y):
    try:
        #attempt
        z=x/y
        print(f'Result : {z}')
    except:
        #Catch
        print(f'Something bad happened x:{x}, y:{y}')
    finally:
        #moving along
        print(f'Complete')

test_one(100, 20)
test_one(5, 0)
test_one(5, 'cat')

@outline
def test_two(x,y):
    try:
        #attempt
        assert (x > 0)
        assert (y > 0)
    except AssertionError:
        print(f'Failed to assert x:{x}, y:{y}')
    except TypeError:
        print(f'Wrong Type x:{x}, y:{y}')
    except Exception as e:
        #Catch
        print(f'Something bad happened x:{x}, y:{y}, Exception:{e}')
    else:
        #trusted code
        z=x/y
        print(f'Result : {z}')
    finally:
        #moving along
        print(f'Complete')


test_two(100, 20)
test_two(5, 0)
test_two(5, 'cat')

#User Defined exceptions and raising
class CatError(RuntimeError):
    def __init__(self, *args):
        self.args = args

@outline
def test_cat(qty):
    try:
        if not isinstance(qty,int):
            raise TypeError('Must be an Int type')
        if qty < 9:
            raise CatError('Must own more than 9 cats')
    except Exception as e:
        print(f'Oops, {e.args}')
    finally:
        print(f'Complete')

test_cat(3)
test_cat(12.3)
test_cat(11)
test_cat('abc')
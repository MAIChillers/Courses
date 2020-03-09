"""
Mymodule it's a simple example.

The module declared functions that display the names of functions
"""
def hello():
    """print hello"""
    print("hello")


def world():
    """print world"""
    print('world')

def my():
    """print my"""
    print('My')

pi = 5
e = 1
_a = 20

# __all__ = ['hello', 'world', 'e']

print(__name__)
if __name__ == '__main__':
    print('Hello world!')

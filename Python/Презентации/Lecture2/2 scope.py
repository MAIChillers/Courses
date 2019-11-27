def foo():
    x = 10
    print(x)
    hello = 'hello'


def foo1():
    print(x)


def foo2():
    global x
    x = 15
    print(x)

def foo3():
    x = 2
    def foo4():
        nonlocal x
        x = 5
        print('foo4', x)
    foo4()
    print('foo3', x)

x = 5
hello = 1
foo()
foo1()
foo2()
print(x)
foo3()

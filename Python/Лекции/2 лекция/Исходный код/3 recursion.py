def foo(n):
    print(n)
    if n > 0:
        foo(n - 1)
    print(n)

def fib(n):
    if n <= 0:
        return 0
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

foo(5)

fib(6)






















def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def factorialRecurs(n):
    if n < 2:
        return 1
    return factorialRecurs(n - 1) * n

factorial(5)
factorialRecurs(5)












def fibonachi(n):
    if n < 3:
        return 1
    fibLast = 1
    fibCurrent = 1
    for i in range(n - 2):
        fibLast, fibCurrent = fibCurrent, fibCurrent + fibLast
    return fibCurrent


def fibonachiRec(n):
    if n <= 0:
        return 0
    if n < 3:
        return 1
    return fibonachiRec(n - 1) + fibonachiRec(n - 2)

fibonachi(5)
fibonachiRec(5)

import sys
print(sys.maxsize)

def divide(a):
    for i in range(2, (a // 2) + 1):
        if not a % i:
            return False
        return True

l = []
for i in range(1000000000000000):
    l.append(i)
l

iterPrime = (x for x in range(1000000000000000) if divide(x))
list(iterPrime)
next(iterPrime)

sum(x for x in range(100000) if divide(x))


list1=[-2,-1,0,1,2,3,4,5]
myGen = (i for i in list1) # выражение-генератор
myList = list(myGen)
print(myList)
print(myGen)

myList = [ x**2 for x in range(23) if not x % 3]
print(myList) # [0, 9, 36, 81, 144, 225, 324, 441]

mySet = { (x%3)**2 for x in range(25) if x % 2 == 0}
print(mySet) # {0, 1, 4}

myDict = {x: x**2 for x in myList}
print(myDict)

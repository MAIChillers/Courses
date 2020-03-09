mySet = set([1, 5, 0, -2, 9])
sorted(mySet)
print(mySet)
sorted(mySet, reverse=True)
print(mySet)


myTupleStr = ('Hello', 'World', 'Spam', 'Python')
sorted(myTupleStr)


myStr1 = 'Hello '
myStr2 = 'World!!!!'
myStr3 = myStr1 + myStr2
print(myStr3)

myTuple1 = (1, 2, 3)
myTuple2 = (5, 1)
myTuple3 = myTuple1 + myTuple2
print(myTuple3)

myList1 = [1, 4, 5]
myList2 = [10, 8, 30]
myList3 = myList1 + myList2
print(myList3)


myDict1 = {'a': 1, 'b': 2}
myDict2 = {'c': 3, 'd': 4}
myDict3 = myDict1.copy()
myDict3.update(myDict2)
print(myDict3)


# Объединение
mySetA = {1, 2}
mySetB = {2, 4}

mySetC = mySetA.union(mySetB)
mySetC = mySetA | mySetB
print(mySetC)

# Пересечение
mySetC = mySetA.intersection(mySetB)
mySetC = mySetA & mySetB
print(mySetC)

# Разность
mySetC = mySetA.difference(mySetB)
mySetC = mySetA - mySetB
print(mySetC)

# Симметричная разность
mySetC = mySetA.symmetric_difference(mySetB)
mySetC = mySetA ^ mySetB
print(mySetC)

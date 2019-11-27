myList = [1, 2, 3]
myStr = 'Hello world'
mytuple = (1, 2, 3)
mySet={1,2,3,3}
myFSet = frozenset(myStr)
mydict = {1: 'a', 2: 'b', 3: 'c', 3: 'f'}


print(myList)
print(myStr)
print(mytuple)
print(mySet)
print(myFSet)
print(mydict)


len(myList)
max(myStr)
min(mydict.items())()
sum(myFSet)

'H' in myStr


for item in myList:
    print(item)

for item in myFSet:
    print(item)


for item in myList:
    if item == 1:
        myList.append(5)
    if item == 2:
        myList.insert(0, 7)
    print(item)

for item in list(myList):
    if item == 1:
        myList.append(5)
    if item == 2:
        myList.insert(0, 7)
    print(item)

print(myList)

##  Индексированные коллекции
myList=[1,2,3,3,5,7,1]
print(myList.count(1))
print(myList.index(1))

myList = [1, 2, ['H', 'E', 'L', 'O']]
myCopyList = myList.copy()
print(myList, myCopyList)
myCopyList[2][0] = 'I'
myCopyList[0] = 0
print(myList, myCopyList)



## Конвертация из одного типа в другой
myTuple=(1,2,3,3,5,7,1)
myList = list(myTuple)
mySet = set(myTuple) # Потеряем дубликаты
myFrozenset = frozenset(myTuple) # Потеряем дубликаты
print(myList, mySet, myFrozenset)


myTuple=(1,2,3,3,5,7)
myStr = 'Hello World'
print(list(zip(myTuple, myStr)))
myDict = dict(zip(myTuple, myStr))
myDict

myList = [1, 2, 3, [1, 2]]
mySet = set(myList)

def hash(x):
    return x % 5

l = [0, 0, 0, 0, 0]
num = 3
l[hash(num)] = num
l
num = 5
l[hash(num)] = num
l

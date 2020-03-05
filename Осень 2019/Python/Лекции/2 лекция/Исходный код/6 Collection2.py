myList = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4 ,5)
myStr = "Hello World!"
my2List = [[1, 2], [3, 4]]

print(myList[1], myList[-2])
print(mytuple[1], mytuple[-2])
print(myStr[1], myStr[-2])
print(my2List[0][1])

my2List[0][1] = 10
my2List

# Срезы  Slice
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mytuple = (1, 2, 3, 4 ,5)
myStr = "Hello World!"


myList[1: -1: 2]
myList[ :5:3]
myStr[1::2]
myStr[1:5]
mytuple[:]

averageDailyTemp = (1.0, 0.0, 0.6, -0.5, -0.1, -0.4, 1.0, 4.0, 2.0, 1.0, 5.5,
                    2.0, 10, 12, 10.3, 21, 0, -24, -5, -4.5, -4.4, -.4, -.5,
                    -5.1, -2.1, 2.0, 2.1, 1.0, 1.4, 1.6)

newList = averageDailyTemp[2:9]
print(newList)

firstWeek, secondWeek, secondToend = slice(2, 9), slice(8, 15), slice(8, None)
newList = averageDailyTemp[firstWeek]
print(newList)


myList[1:5] = [10]
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList[1:5] = [100, 200, 300, 400, 500, 600]
myList
myList[1:5] = []
myList





myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList[100]
myList[-100]

myList[10:100]
myList[10:-100]

sum = lambda x,y:x+y
sum(1, 2)


strNum = ['1', '2', '3']
listNum = list(map(int, strNum))
listNum

x = list(map(int, input().split()))
x



tempF = [32, 50, 8.2]
tempC = list(map(lambda t: 5/9 * (t - 32), tempF ))
tempC


myTuple = (1, 2, 3, 3, 5, 7)
myStr = 'Hello World'
print(list(zip(myTuple, myStr)))

myDict = dict(zip(myTuple, myStr))
myDict

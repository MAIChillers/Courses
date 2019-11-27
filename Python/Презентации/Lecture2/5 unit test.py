def bublesort(listOfContent):
    N = len(listOfContent)
    for i in range(N-1):
      for j in range(N-i-1):
          if listOfContent[j] > listOfContent[j+1]:
            buff = listOfContent[j]
            listOfContent[j] = listOfContent[j+1]
            listOfContent[j+1] = buff


def test_bublesort():
    test = [[85, 78, 73, 44, 21],
            [1, 2],
            [1],
            []
           ]
    resTest = [[21, 44, 73, 78, 85],
               [1, 2],
               [1],
               []
              ]
    for i in range(len(test)):
        bublesort(test[i])
        if test[i] == resTest[i]:
            print("Test {} OK".format(i))
        else:
            print("Test {} fail, result: {}, true: {}".format(i, test[i],
                                                              resTest[i]))

test_bublesort()









def getQuantyEven(listOfContent):
    quanty = 0
    for item in listOfContent:
        if item % 2 == 0:
            quanty += 1
    return quanty


def test_getQuantyEven():
    test = [[85, 78, 73, 44, 21],
            [1, 2],
            [1]
           ]
    resTest = [2, 1, 0]
    for i in range(len(test)):
        if getQuantyEven(test[i]) == resTest[i]:
            print("Test {} OK".format(i))
        else:
            print("Test {} fail, result: {}, true: {}".format(i, test[i],
                                                              resTest[i]))


test_getQuantyEv\en()

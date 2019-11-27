

def bublesort(listOfContent):
    N = len(listOfContent)
    for i in range(N-1):
      for j in range(N -i-1):
          if listOfContent[j] > listOfContent[j+1]:
            buff = listOfContent[j]
            listOfContent[j] = listOfContent[j+1]
            listOfContent[j+1] = buff



content = [62, 60, 96, 87, 32, 100]
bublesort(content)
print(content)

content2 = [33, 11, 8, 4, 9, 100]
bublesort(content2)
print(content2)

def bublesort(listOfContent):
    N = len(listOfContent)
    for i in range(N-1):
      for j in range(N-i-1):
          if listOfContent[j] > listOfContent[j+1]:
            buff = listOfContent[j]
            listOfContent[j] = listOfContent[j+1]
            listOfContent[j+1] = buff



bublesort(1)




try:
    k = 1/0
except TypeError as z:
    print(z)
except Exception:
    print('Error')
else:
    print("Этот код будет выполнять только тогда, когда нет исключения")
finally:
    print("Этот код будет всегда выполняться")









def foo():
    k = 1/0
    raise Exception("QWER")


try:
    foo()
except ArithmeticError:
    print("Арифметическая ошибка")
except Exception:
    print("Какое-то исключение")
else:
    print("Ошибок не было")
finally:
    print("The End")

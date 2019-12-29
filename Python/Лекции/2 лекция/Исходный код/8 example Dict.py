u"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.

Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.

Примеры
входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod
выходные данные
Ukraine
Russia
Russia

"""

listOfCountry = [['Russia', 'Moscow', 'Petersburg', 'Novgorod', 'Kaluga'],
                 ['Ukraine', 'Kiev', 'Donetsk', 'Odessa']]
listOfCity = ['Odessa', 'Moscow', 'Novgorod']

dictOfCountry = dict()

for i in listOfCountry:
    for j in i[1:]:
        dictOfCountry[j] = i[0]

print(dictOfCountry)

for i in listOfCity:
    print(dictOfCountry[i])






def foo():
    x = 10
    print("foo", x)
    def foo1():
        nonlocal x
        print("foo1", x)
        x = 7
    foo1()
    print("foo", x)

x = 5
foo()
print(x)

u"""Задача с собеседования в Яндекс.

Дан массив целых чисел

Требуется написать программу, позволяющую сказать, есть ли в массиве,
такой подмассив, что сумма его элементов равна K

Ввод	          Вывод
2 5 8 10          True
7
"""


def foo(nums, k):
    sum = 0
    setSumSubArray = set()
    for i in nums:
        sum += i
        if sum == k or sum - k in setSumSubArray:
            return True
        else:
            setSumSubArray.add(sum)
    return False


foo([2, 5, 8, 10], 7)

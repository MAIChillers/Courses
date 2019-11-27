FILENAME = 'example1.txt'
try:
    handle = open(FILENAME, 'r')
    try:
        pass
    except IOError:
        print('Что-то пошло не так при работе с файлом')
    finally:
        handle.close()
except IOError:
    print('Нет доступа к файлу')
except Exception as e:
    print(e)



FILENAME = 'example.txt'
try:
    handle = open(FILENAME, 'r')
    with open(FILENAME, 'r') as handle:
        pass # работа с файлами
except IOError:
    print('Ошибка при работе с файлом')

import os
os.getcwd()


FILENAME = 'example.txt'
try:
    handle = open(FILENAME, 'r')
    try:
        allFileStr = handle.read()
        print(allFileStr)
    except IOError:
        print('Что-то пошло не так при работе с файлом')
    finally:
        handle.close()
except IOError:
    print('Нет доступа к файлу')
except Exception as e:
    print(e)


FILENAME = 'example.txt'
try:
    handle = open(FILENAME, 'r')
    try:
        oneFileLine = handle.readline()
        allFileLine = handle.readlines()
        print(oneFileLine)
        print(allFileLine)
    except IOError:
        print('Что-то пошло не так при работе с файлом')
    finally:
        handle.close()
except IOError:
    print('Нет доступа к файлу')
except Exception as e:
    print(e)



FILENAME = 'example.txt'
try:
    handle = open(FILENAME, 'r')
    try:
        for line in handle:
            print(line, end='')
    except IOError:
        print('Что-то пошло не так при работе с файлом')
    finally:
        handle.close()
except IOError:
    print('Нет доступа к файлу')
except Exception as e:
    print(e)


FILENAME = 'example1.txt'
try:
    handle = open(FILENAME, 'w')
    try:
        handle.write("Hello world\n")
        listofStr = ["This File is Test\n", 'Test is good\n', "GoodBye\n"]
        handle.writelines(listofStr)
    except IOError:
        print('Что-то пошло не так при работе с файлом')
    finally:
        handle.close()
except IOError:
    print('Нет доступа к файлу')
except Exception as e:
    print(e)

import numpy as np
a = np.array([1, 2, 3])
a

b = np.array([[1.5, 2, 3], [4, 5, 6]])
b

c = np.array([1.5, 2, 3], dtype=np.complex)
c

import numpy as np
zero = np.zeros((3, 5), dtype=np.float64)
zero

one = np.ones((3, 5), dtype=np.int)
one

empt = np.empty((2, 3), dtype=np.complex)
empt

eye = np.eye(4)
eye

np.arange(10, 30, 5)
np.arange(1.0, 2.0, 0.2)  # Числа от 1 до 2 не включительно, с шагом 0.2

np.linspace(0, 2, 9) # 9 чисел от 0 до 2 включительно



def f1(i, j):
    return (i + 1 * j + 1) ** 2


np.fromfunction(f1, (3, 4))

b.ndim
b.shape
b.size
b.dtype



a = np.array([20, 30, 40, 50, 60])
b = np.array([1, 2, 3, 4, 5])
a
b
a + b
a - b
a * b
a / b

a ** b
a % b

a < b



a = np.array([20, 30, 40, 50, 60])
b=5
a + b
a - b
a < 35

np.cos(a)

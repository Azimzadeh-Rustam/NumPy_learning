import numpy as np

# Создание одномерного массива из произвольных 10 чисел
array1 = np.empty(10, dtype = 'int16')
print(array1)

# Создание двумерного массива из произвольных 10 чисел
array2 = np.empty((3, 2), dtype = 'int16')
print(array2)

# Создание двумерного массива состоящий полностью из -1
array3 = np.full((3, 2), -1)
print(array3)

# Создание матриц
array4 = np.mat('1 2 3 4')
print(array4)

array5 = np.mat('1 2; 3 4')
print(array5)

array6 = np.mat([5, 4, 3])
print(array6)

array7 = np.mat( [(1, 2, 3), (4, 5, 6)] )
print(array7)

# Создание диагональной матрицы (если передаем одномерный список)
array8 = np.diag([1, 2, 3])
print(array8)
# Выделение диагональных элементов (если передаем массив)
array9 = np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(array9)

array10 = np.linspace(0, np.pi, 5)
print(array10)

array11 = np.logspace(0, 1, 3)
print(array11)

array12 = np.geomspace(1, 16, 5)
print(array12)

# Формирование массива на основе итерируемого объекта (в данном случае - строки)
array13 = np.fromiter("hello", dtype = 'U1')
print(array13)

array14 = np.fromstring('1 2 3 4 5', dtype = 'int16', sep = ' ')
print(array14)

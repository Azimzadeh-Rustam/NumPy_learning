import numpy as np

# Создаем массив с явным указанием типа переменных
array = np.array([1, 2, 3, 4, 5], 'float64')
print(array)

# Запись в комплексной форме
complexNum = np.complex64(10)
complexArr = np.complex64(array)
print(complexNum)
print(complexArr)

array2D = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])
print(array2D)
# Выводим сроки двумерной матрицы
print(array2D[0])
print(array2D[1])
print(array2D[2])

array3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(array3D)
# Выводим срезы трехмерной матрицы
print(array3D[0])
print(array3D[1])
print(array3D[2])
# Выводим первую строку первого среза
print(array3D[0, 0])
# Выводим первый элемент первой строки первого среза
print(array3D[0, 0, 0])
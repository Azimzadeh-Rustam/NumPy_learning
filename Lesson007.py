import numpy as np

array1 = np.arange(10)

# Срезы массивов numpy возвращают их представления
array2 = array1[2:4]
print(array2)

array2 = array1[::3]
print(array2)

array2 = array1[::-3]
print(array2)

array1[:4] = [-11, -12, -13, -14]
print(array1)

array1[4::2] = np.array([10, 20, 30])
print(array1)

matrix = np.array([(1, 2, 3), (10, 20, 30), (100, 200, 300)])
print(matrix)

# matrix[0] = matrix [0,:]
first_row = matrix[0]
print(first_row)

second_column = matrix[:,1]
print(second_column)

matrix4D = np.arange(1, 82).reshape(3, 3, 3, 3)
# matrix4D[:, :, 1, 1] = matrix4D[..., 1, 1] (удобно в случае многомерных массивов)
print(matrix4D[..., 1, 1])

# При списочной индексации в переменную передается копия данных (создается новый независимый массив)
array3 = array1[[0]]
print(array3)

array3 = array1[[0, 4, 7, 0]]
print(array3)

# Присваиваем соответствующим индексам определенные значения
array1[[0, 1, 7, 5]] = [45, 82, 33, 43]
print(array1)

indexes = [0, 5, 3, 7]
print(array1[indexes])
indexes = np.array([0, 5, 3, 7]) # тоже самое, просто через массив numpy
print(array1[indexes])

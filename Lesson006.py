import numpy as np

array1 = np.array([(1, 2), (3, 4)])
array2 = np.array([(5, 6), (7, 8)])

# Объединение массивов по горизонтали
array3 = np.hstack([array1, array2])
print(array3)
# Объединение массивов по вертикали
array4 = np.vstack([array1, array2])
print(array4)

array5 = np.fromiter(range(5), dtype= 'int32')
array6 = np.fromiter(range(5, 10), dtype= 'int32')

array7 = np.column_stack([array5, array6])
print(array7)

array8 = np.row_stack([array5, array6])
print(array8)

array9 = np.arange(1, 13)
array9.resize(3, 3, 2)
array10 = np.arange(13, 26)
array10.resize(3, 3, 2)

# Объединение по какой-то конкретной оси (вдоль какой-то определенной оси)
array11 = np.concatenate([array9, array10], axis = 0) # размерность 6x3x2
print(array11.shape)
array12 = np.concatenate([array9, array10], axis = 1) # размерность 3x6x2
print(array12.shape)
array13 = np.concatenate([array9, array10], axis = 2) # размерность 3x3x4
print(array13.shape)

array14 = np.arange(10)
# Разделение по горизонтали
np.hsplit(array14, 2)

array14.shape = 10, -1
# Разделение по вертикали
np.vsplit(array14, 2)

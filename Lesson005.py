import numpy as np

array1 = np.arange(10)
array1.shape = 2, 5

# Преобразование многомерного массива в одномерный (вектор)
array2 = array1.ravel() # по ссылке
array1.shape = -1 # сам по себе
print(array1)

# Изменение представления текущего массива
array1.resize(2, 5)
print(array1)

array1.resize(4, 5, refcheck = False)
print(array1)

array = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
print(array)

# Транспонирование матрицы
arrayTransposed = array.T
print(arrayTransposed)

# Чтобы можно было транспонировать вектор, нужно к нему добавить еще одну ось
x = np.arange(10)
x.shape = 1, -1
print(x.T)

array3D = np.arange(32).reshape(8, 2, 2)
print(array3D.shape)

# Добавление новой оси
array4D = np.expand_dims(array3D, axis = 0) # создаем новое представление
print(array4D.shape)

# Удаляет из массива все оси где всего один элемент
array3 = np.squeeze(array4D)
print(array3.shape)

# Удаляет определенную ось, которая содержит один элемент
array4 = np.squeeze(array4D, axis = 0)
print(array4.shape)

array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array6 = array5[np.newaxis, :]
print(array6.shape)
print(array6)

array7 = array5[:, np.newaxis]
print(array7.shape)
print(array7)

array8 = array5[np.newaxis, : , np.newaxis]
print(array8.shape)
print(array8)

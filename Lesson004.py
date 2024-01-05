import numpy as np

array = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
print(array.dtype)

array.dtype = np.int8()
print(array)

print(array.size)
print(array.itemsize)

array2 = np.ones( (3, 4, 5) )
print(array2.ndim) # Размерность массива
print(array2.shape) #Количество элементов по каждой оси
array2.shape = 60 # Можно также менять количество элементов по каждой оси (но общее количество элементов должно быть прежним)
print(array2)
array2.shape = 12, 5
print(array2)

# Новый массив ссылается на другое представление тех же данных
# тоесть, если изменить изначения в одном массиве, то их представление поменяется и в другом
array3 = array2.reshape(3, 2, 10)
print(array3)

# Чтобы избежать неожиданных ошибок при изменении каких-то данных в родительском,
# используют метод, который создает новую, независимую копию представления
array4 = array2.view()

# Создание новой, независимой копии данных
array5 = array2.copy()
array6 = np.array(array2) # тоже самое
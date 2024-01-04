import numpy as np

#Передаем список [1, 2, 3, 4, 5, 6, 7, 8, 9],
# который команда array() из пакета numpy преобразовывает в одномерный массив
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Выводим тип элементов массива
print(array.dtype)

# Обращение к конкретному элементу массива
# <имя массива>[<кортеж индексов>]
print(array[0])

# Возвращает новый массив, который состоит из элементов на месте которых стоит True
print(array[ [False, True, False, True, True, True, False, True, True] ])

# Представляем одномерный массив в виде двумерного
array = array.reshape(3, 3)
print(array)

# Обращение к конкретному элементу двумерного массива
print(array[0][1])
print(array[0, 1])

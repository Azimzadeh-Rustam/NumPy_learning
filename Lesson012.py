import numpy as np

array = np.array([1, 2, 3, 4, 4, 3, 2])

set = np.unique(array) # преобразуем массив во множество (все элементы уникальны)
print(set)
print(np.unique(array, return_counts=True))
print(np.unique(array, return_index=True))
print(np.unique(array, return_inverse=True))

x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.intersect1d(x, y)) # Пересечение множеств
print(np.union1d(x, y)) # Объединение двух множеств
print(np.setdiff1d(x, y)) # Вычитание множеств
print(np.setxor1d(x, y)) # Ассиметричная разность

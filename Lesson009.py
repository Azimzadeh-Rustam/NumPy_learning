import numpy as np

array = np.array([1, 2, 3, 10, 20, 30])

print(array[array > 5])

array2 = np.array([1, 2, 3, 4, 5, 6])
print(array == array2)
print(array != 2)

print(np.greater(array, array2))
print(np.less(array, array2))
print(np.equal(array, array2))

print(np.array_equal(array, array2))

# Если хотя бы один эдемент ассива больше 5
print(np.any(array > 5))

# Если все элементы массива удовлетворяют условию (в данном случае больше 5)
print(np.all(array > 5))

# Сумма всех эллементов массива
print(array.sum())

array3 = np.array([ 1, 2, np.nan, -np.inf, np.inf])
print(np.isinf(array3))
print(np.isnan(array3))

# Отфильтруем все значения inf из массива
indx = np.isinf(array3)
print(array3[~indx]) # ~ интертируем массив, а значит вызываются все которое не inf

# Оставляем только все конечные значения в массиве
indx = np.isfinite(array3)
print(array3[indx])

array4 = np.array([1 + 2j, 3 - 4j, 5])
print(np.iscomplex(array4))
print(np.isreal(array4))

X = np.array([True, False, True, False])
Y = np.array([True, True, False, False])
print(np.logical_and(X, Y))
print(np.logical_or(X, Y))
print(np.logical_not(X))
print(np.logical_xor(X, Y))

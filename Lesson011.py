import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)

# Поэлементное умножение соответствующих элементов матриц
print (a * b)

# Матричное умножение
print(np.matmul(a, b))

a = np.arange(1, 10)
b = np.ones(9)
# Векторное умножение
print(np.inner(a, b))
print(np.outer(a, b))


print(a @ b)
a.resize(3, 3)
b.resize(3, 3)
print(a @ b)

a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
print(np.linalg.matrix_rank(a)) # нахождение ранга матрицы
y = np.array([10, 20, 30])
print(np.linalg.solve(a, y)) # решение линейнго уровнения

invA = np.linalg.inv(a) # Обратная матрица
x = invA @ y
print(x)

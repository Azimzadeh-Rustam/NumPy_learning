import numpy as np

array1 = np.array([1, 2, 3, 10, 20, 30])

print(array1.sum()) # Сумма всех элементов массива
print(array1.mean()) # Среднее арифмитическое всех значений
print(array1.max())
print(array1.min())

array1.resize(3, 2)
print(array1)
print(array1.sum())
print(array1.sum(axis=0)) # Сумма всех элементов по столбцам
print(array1.sum(axis=1)) # Сумма всех элементов по рядам
print(array1.max(axis=0)) # Максимальные значения в каждом столбце
print(array1.max(axis=1)) # Максимальные значения в каждом ряду

array2 = np.array([-1, 1, 5, -44, 32, 2])
print(np.abs(array2))
print(np.abs(-10.5))
print(np.amax(array2))
print(np.amin(array2))
print(np.around(7.1)) # Округление числа до ближайшего целого
print(np.argmax(array2)) # находит индекс соответствующий максимальному элементу массива
print(np.argmin(array2))
array2.resize(3, 2)
print(np.amax(array2, axis=0))

array3 = np.linspace(0, np.pi, 10) # Массив от 0 до pi с разбиением по 10 значений
print(array3)
print(np.sin(array3))
print(np.cos( [0, 1.57, 3.14] ))

print(np.random.rand()) # Генерирует случайное число от 0 до 1 (1 не включается)
print(np.random.rand(5))
print(np.random.rand(2, 3))
print(np.random.randint(10)) # Генерация случайного числа от 0 до 10 (10 не включительно)
print(np.random.randint(5, 10)) # Генерация случайного числа от 5 до 10 (10 не включительно)
print(np.random.randint(5, 10, size=5))
print(np.random.randint(5, 10, size=(2, 5)))

array4 = np.arange(10)
np.random.shuffle(array4) # перетасовываем случайным образом элементы массива (работает только по первой оси)
np.random.permutation(10) # Создает массив с заданным набором элементов, перетасованных случайным образом

x = np.array([1, 4, 3, 7, 10, 8, 14, 21, 20, 23])
y = np.array([4, 1, 6, 9, 13, 11, 16, 19, 15, 22])
print(np.median(x)) # медиана случайно величины
print(np.var(x)) # дисперсия случайно величины
print(np.std(x)) # среднеквадратическое отклонение случайно величины

XY = np.vstack([x, y])
print(XY)
print(np.corrcoef(XY)) # коэффициент корреляции Пирсона
print(np.cov(XY)) # автокореляционная матрица
print(np.correlate(x, y)) # взаимная корреляция между двумя векторами

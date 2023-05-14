# Целые числа (int)
a = 5
b = -3

# Вещественные числа (float)
c = 3.14
d = -0.5

# Булевы значения (bool)
e = True
f = False

# Строки (str)
g = "Hello, World!"
h = 'Python'

# Списки (list)
i = [1, 2, 3, 4, 5]
j = ['apple', 'banana', 'cherry']

# Кортежи (tuple)
k = (1, 2, 3)
l = ('one', 'two', 'three')

# Изменение элемента списка
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# Ошибка при попытке изменить элемент кортежа
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

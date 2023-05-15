# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:                                               Вывод:                    Диапозон:
# [-5, *9, 0, 3, -1, -2, 1, 4, -2, *10,                  [1, 9, 13, 14, 19]     [7 - 10]
#   2, 0, -9, *8, *10, -9, 0, -5, -5, *7]


list = [-5, 9, 0, 3, -1, -2, 1,4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_n = 7
max_n = 10
list_n = []
for i in range(len(list)):
    if min_n <= list[i] <= max_n:
        list_n.append(i)
print(list_n)
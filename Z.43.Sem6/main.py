# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:           Вывод:
# 1 2 3 2 3           2
def Input_list():
    list = []
    num = int(input('Введите длинну списка: '))
    for i in range(num):
        list.append(input(f"Введите {i + 1} число: "))
    return list

#list = Input_list()
list = [1,2,3,2,3,2]
def Coced(list):
    count = 0
    for i in range(len(list) - 1):
        for j in range (i + 1,len(list)):
            if list[j] == list[i]:
                count += 1
    return count
print(Coced(list))
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def I():
    num = int(input('Введите число: '))
    return num

a = {}  # 3, 1, 3, 4, 2, 4,12
b = {}    # 4, 15, 43, 1, 15 
n = I()
for i in range(n):
    a.add('I()')
m = I()
for i in range(m):
    b.add('I()')
print(a,b)
i = a.intersection(b) # пересечение 'a' и 'b'
print(i)

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1: 
#   set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
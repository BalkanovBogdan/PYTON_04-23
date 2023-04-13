# import random as rnd
# n = int(input('Ведите количество дней: '))
# mas = []
# count = 1
# max = 0
# for i in range(n):
#    mas.append(rnd.randint(-50,51))
# print(mas)
# for i in range(1,n):
#     if(mas[i] > 0 and mas[i-1] > 0):
#         count += 1
#         if max < count:
#             max = count
#     if(mas[i] <= 0):
#         count = 1
# print(max)

n = int(input('Введите количество дней: '))
count = 0
max = 0
i = 1
while(i <= n):
    a =int(input('Температура: '))
    i += 1
    if(a > 0):
        count += 1
    if(count > max):
        max = count
    if(a <= 0):
        count = 0
print(max)

# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while

a = int(input())
sum = int(1)
i = int(1)
while(i <= a):
    sum *= i
    i += 1
print(sum)
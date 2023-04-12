# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
n = int(input('Введите номер билета: '))
a1 = int(n//1000)
a2 = int(n%1000)
sum = int(0)
sum2 = int(0)
while(a1 != 0):
    sum += a1%10
    a1 = a1//10
while(a2 != 0):
    sum2 += a2%10
    a2 = a2//10
if sum == sum2:
    print('yes')
else:
    print('no')
a = int(input('Введите год, проверим високосный он или нет -> '))
if(a % 4 == 0 or a % 400 == 0) and (a % 100 != 0 ):
    print('YES')
else:
    print('NO')
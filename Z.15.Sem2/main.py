n = int(input('Введите количество арбузов: '))
min = int(111111111111111110)
max = int(0)
i = int(0)
while(i < n):
    a = int(input('Введите вес арбуза: '))
    i += 1
    if(max < a ):
        max = a
    elif(min > a):
        min = a
print(f"Самый тяжелый арбуз {max} и самый легкий {min}")
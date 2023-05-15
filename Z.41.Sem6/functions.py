def Input():
    num = int(input('введите число: '))
    return num

def Input_list():
    list = []
    num = int(input('Введите длинну списка: '))
    for i in range(num):
        list.append(input(f"Введите {i + 1} число: "))
    return list
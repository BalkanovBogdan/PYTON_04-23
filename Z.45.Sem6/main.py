# Два  различных  натуральных  числа n  и  m  называются дружественными,  если  сумма  делителей 
# числа n(включая  1,  но  исключая  само n)  равна  числу m  и наоборот.
# Например, 220 и 284 – дружественные числа.По данному числу k выведите все пары дружественных 
# чисел, каждое из которых не превосходит k. Программаполучает  на  вход  одно  натуральное  
# число k,  непревосходящее  10^5.  Программа  должна  вывести    все пары  дружественных  чисел,
# каждое  из  которых  непревосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена  только  один  раз  (перестановка  чисел  новую пару не дает).
# Ввод:                   Вывод:
# 300                     220 284

def Del(num: int) -> int:
    summa = 0
    for i in range(1,num // 2 + 1):
        if num % i == 0 :
            summa += i
    return summa

k = int(input(': '))
for num_1 in range(2,k):
    num_2 = Del(num_1)
    if (Del(num_2) == num_1) and (num_1 < num_2):
        print(num_1,num_2)


# СЛОЖНЕЕ ВАРИАНТ 
def slovsri(end_range):        
    dict = {}
    for i in range(2, end_range + 1):
        sum_i = 0
        for j in range(1, (i//2) + 1):
            sum_i = sum_i + j if i % j == 0 else sum_i
        dict[i] = sum_i
    return dict

def dict_frendliy_values(source_dict):
    set_values = set()
    for i in range(2, len(source_dict)):
        for j in source_dict.values():
        # for j in range(len(source_dict)):
            if i == source_dict.get(j) and j == source_dict.get(i) and i != j:
                set_values.add(i)
                set_values.add(j)
    return set_values

number = k
dict = slovsri(number)
print(dict_frendliy_values(dict))
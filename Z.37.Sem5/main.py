# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы(даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3

def sort(n):
    num = input()
    if n == 1:
        return num
    return sort(n - 1) + ' ' + num

print(sort(1))
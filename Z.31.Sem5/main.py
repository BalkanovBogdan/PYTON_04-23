# Последовательностью   Фибоначчи   называетсяпоследовательность чисел a0, a1, ..., an, ...,
# гдеa0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(n):
    if n [0,1]:
        return 1
    return fib(n - 1) + fib(n -2)
number = int(input("Введите число n : "))
print(fib(number))

n = int(input('Растояние можем пройти в день: '))
m = int(input('Растояние нужно пройти: '))
# res = (m + (n - 1)) // n
# res = (m // n) + bool(m % n)
res = -(-m // n)

print(f'Нужно потратить дней на растояние -> {res}')
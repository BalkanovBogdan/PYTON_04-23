# Напишите  программу,  которая  принимает  на  входстроку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n. .split()
list = ("a a a b c a a d c d d").split()
slovar = {}
for i in list:
    if i in slovar:
        print(f'{i}_{slovar[i]}')
        slovar[i] += 1
    else:
        print(f'{i}')
        slovar[i] = 1

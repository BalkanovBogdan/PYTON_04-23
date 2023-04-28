list = [1,2,3,4,5]
k = 3
# for i in range(k):
#     list.append(list.pop(0))
# print(list)

# for i in range(k):
#     list.insert(0, list.pop())
# print(list)

print(list[ -k :] + list[:-k])

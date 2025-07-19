lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for _ in range(lst.count(0)):
    lst.remove(0)
    lst.append(0)
print(lst)


lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
lst_zero = []
for elem in lst.copy():
    if elem == 0:
        lst.remove(elem)
        lst_zero.append(0)
lst.extend(lst_zero)
print(lst)


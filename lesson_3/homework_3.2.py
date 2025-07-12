lst = []
if len(lst) > 1:
    new_lst = lst.pop(-1)
    lst.insert(0, new_lst)
print(lst)



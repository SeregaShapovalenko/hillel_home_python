lst = []
length_lst = len(lst) // 2
if len(lst) % 2 == 0:
    lst_one = lst [:length_lst]
    lst_two = lst [length_lst:]
    lst_end = lst_one, lst_two
    print(list(lst_end))
elif len(lst) % 2 != 0:
    lst_one = lst [length_lst:]
    lst_two = lst [:length_lst]
    lst_end = lst_one, lst_two
    print(list(lst_end))
elif len(lst) == 0:
    lst_end = lst * 2
import string
user_str = str(input("Введите 2 буквы через дефис: "))
one_letter = user_str[0]
two_letter = user_str[-1]
lst_ascii_letters = string.ascii_letters
index_one = lst_ascii_letters.find(one_letter)
index_two = lst_ascii_letters.find(two_letter)
final_lst = lst_ascii_letters[index_one:index_two + 1]
print(final_lst)

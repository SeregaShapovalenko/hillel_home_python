import keyword
import string
user_str = input("Введите строку: ")
valid = True
if not user_str or user_str[0].isdigit():
    valid = False
else:
    if user_str in keyword.kwlist:
        valid = False
    elif "__" in user_str:
        valid = False
    else:
        for elem in user_str:
            if elem.isupper():
                valid = False
                break
            if elem.isspace():
                valid = False
                break
            if elem in string.punctuation and elem != '_':
                valid = False
                break
print(valid)
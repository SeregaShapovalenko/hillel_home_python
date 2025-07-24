user_str = input("Введите строку: ")
user_str = user_str.strip()
user_str = user_str.title()
not_symbols = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
mod_str_user = ""
for elem in user_str:
    if elem not in not_symbols:
        mod_str_user += elem
hashtag = "#"
hashtag_user_str = f"{hashtag}{mod_str_user}"
if len(hashtag_user_str) > 140:
    hashtag_user_str = hashtag_user_str[:140]
print(hashtag_user_str)
import string
user_str = input("Введите строку: ")
user_str = user_str.strip()
user_str = user_str.lower()
mod_str_user = ""
for elem in user_str:
    if elem not in string.punctuation:
        mod_str_user += elem
words = mod_str_user.split()
mod_str_user = ''.join(word.capitalize() for word in words)
hashtag = "#"
hashtag_user_str = f"{hashtag}{mod_str_user}"
if len(hashtag_user_str) > 140:
    hashtag_user_str = hashtag_user_str[:140]
print(hashtag_user_str)
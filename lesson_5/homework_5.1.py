user_str = input("Введите строку: ")
not_symbols = "!#$%&'()*+,-./:;<=>?@[\\]^`{|}~ "
not_words = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
if (not user_str.isidentifier()
    or "__" in user_str
    or user_str[0] in not_symbols
    or user_str[0] in not_words
    or any(elem.isupper() for elem in user_str)):
    print(False)
else:
    print(True)
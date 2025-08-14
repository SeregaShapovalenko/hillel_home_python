def is_palindrome(text: str) -> bool:

    text = text.casefold()
    cleaning = ''.join(char for char in text if char.isalnum())
    reversed_cleaned = cleaning[::-1]
    result = cleaning == reversed_cleaned
    return result


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
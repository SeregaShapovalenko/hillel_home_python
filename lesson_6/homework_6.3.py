number = input("Введите число: ")
while int(number) > 9:
    result = 1
    for digit in number:
        result *= int(digit)
    number = str(result)
print(number)
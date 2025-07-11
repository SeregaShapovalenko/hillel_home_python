number = int(input("Введите любое 5-и значное число от 0 до 9: "))
number_1 = number % 10
number_2 = number % 100 // 10
number_3 = number % 1000 // 100
number_4 = number % 10000 // 1000
number_5 = number % 100000 // 10000
result = number_1 * 10000 + number_2 * 1000 + number_3 * 100 + number_4 * 10 + number_5
print(result)
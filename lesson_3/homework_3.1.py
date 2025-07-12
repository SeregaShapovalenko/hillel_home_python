number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
action = input("Введите одну из операций  +, -, *, /: ")
if action == "+":
    print(number_1 + number_2)
elif action == "-":
    print(number_1 - number_2)
elif action == "*":
    print(number_1 * number_2)
elif number_2 != 0:
    print(number_1 / number_2)
else:
    print("На ноль делить нельзя, перезапустите программу!")



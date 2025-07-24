while True:
    number_1 = int(input("Введите первое число: "))
    number_2 = int(input("Введите второе число: "))
    action = input("Введите одну из операций  +, -, *, /: ")

    if action == "+":
        print(number_1 + number_2)
    elif action == "-":
        print(number_1 - number_2)
    elif action == "*":
        print(number_1 * number_2)
    elif action == "/":
        if number_2 != 0:
            print(number_1 / number_2)
        else:
            print("На ноль делить нельзя, перезапустите программу!")
    continuation = input("Если хотите продолжить работу с калькулятором, введите 'yes' или 'y': ")
    if continuation not in ("yes", "y"):
        print("Работа калькулятора завершена!")
        break


user_numder = int(input("Введите число не более 8640000: "))
day_in_second = 86400
hour_in_second = 3600
day = user_numder // day_in_second
last_two_digits = day % 100
last_digit = day % 10
if 11 <= last_two_digits <= 14:
    day_word = "дней"
elif last_digit == 1:
    day_word = "день"
elif 2 <= last_digit <= 4:
    day_word = "дня"
else:
    day_word = "дней"
hour = (user_numder - (day * day_in_second)) // hour_in_second
minute = (user_numder - (day * day_in_second) - (hour * hour_in_second)) // 60
sec = user_numder - (day * day_in_second) - (hour * hour_in_second) - (minute * 60)
user_data = f"{str(day)} {day_word}, {str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(sec).zfill(2)}"
print(user_data)
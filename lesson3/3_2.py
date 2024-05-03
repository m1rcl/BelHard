# Пользователь вводит 3 числа,
# найти среднее арифмитическое с точность 3

user_num1 = float(input("Введите первое число: "))
user_num2 = float(input("Введите второе число: "))
user_num3 = float(input("Введите третье число: "))

average = round((user_num1 + user_num2 + user_num3) / 3, 3)

print("Среднее арифметическое трех введенных чисел", average)

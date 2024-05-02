# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

try:
    user_number1 = float(input("Введите первое число: "))
    user_operation = input(
        "Введите необходимый арифметечский оператор над первым числом (+) (-) (*) (/) (**) (//) (%): ")
    if user_operation not in ('+', '-', '*', '/', '**', r'//', '%'):
        raise ValueError
    user_number2 = float(input("Введите второе число: "))

    if user_operation == '+':
        result = user_number1 + user_number2
    if user_operation == '-':
        result = user_number1 - user_number2
    if user_operation == '*':
        result = user_number1 * user_number2
    if user_operation == '/':
        result = user_number1 / user_number2
    if user_operation == '**':
        result = pow(user_number1, user_number2)
    if user_operation == '//':
        result = user_number1 // user_number2
    if user_operation == '%':
        result = user_number1 % user_number2

    print("Результат операции: ", result)
except ValueError:
    print("Введены не числа или введен неизвестный оператор")
except ZeroDivisionError:
    print("Ошибка деления на ноль")

# Вывести первые N цисел кратные M и больше K

try:
    number = int(
        input("Введите целое число больше которого должны быть выводимые числа: "))
    count_numbers = int(input("Введите количество выводимых чисел: "))
    if count_numbers <= 0:
        raise ValueError
    multiplicity_number = int(
        input("Введите целое число которому должно быть кратны выводимые числа: "))
    if multiplicity_number <= 0:
        raise ValueError

    while count_numbers > 0:
        if not (number % multiplicity_number):
            print(number, end=" ")
            count_numbers -= 1
        number += 1
except ValueError:
    print("Введены неверные данные")

# Вывести первые N цисел кратные M и больше K

try:
    number = int(
        input("Введите минимальное (начальное) целое число: "))
    count_numbers = int(input("Введите количество выводимых чисел: "))
    if count_numbers <= 0:
        raise ValueError
    multiplicity_number = int(
        input("Введите число на кратность которому необходима проверка: "))
    if multiplicity_number <= 0:
        raise ValueError

    print(number, end="")
    while count_numbers > 1:
        number += 1
        if not (number % multiplicity_number):
            print(", ", number, end="")
            count_numbers -= 1
except ValueError:
    print("Введены неверные данные")

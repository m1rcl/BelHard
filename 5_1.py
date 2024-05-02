# Вывести первые N цисел кратные M и больше K

try:
    number = int(
        input("Введите целое число больше которого должны быть выводимые числа: "))
    count_numbers = int(input("Введите количество выводимых чисел: "))
    if count_numbers <= 0:
        raise ValueError
    multiplicity_number = abs(int(
        input("Введите целое число отличное от ноля, которому должно быть кратны выводимые числа: ")))
    if multiplicity_number == 0:
        raise ValueError

    number += 1
    if (number % multiplicity_number):
        number = (number // multiplicity_number + 1) * multiplicity_number
    for _ in range(count_numbers):
        print(number, end=" ")
        number = number + multiplicity_number

except ValueError:
    print("Введены неверные данные")

# **Вывести четные числа от 2 до N по 5 в строку

try:
    count_numbers = int(
        input("Введите чило ДО которого необходимо вывести четные числа: "))
except ValueError:
    print("введено не число")

for number in range(2, count_numbers):
    if not (number % 2):
        print(number, end=" ")
        if not (number % 5):
            print()

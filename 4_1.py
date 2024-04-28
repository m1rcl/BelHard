# Заполнить список степенями числа 2 (от 2^1 до 2^n)

user_input = int(
    input("Введите необходимую степень ДО которой нужно возвести число 2 поочередно: "))

output_list = [pow(2, n) for n in range(1, user_input)]  # ДО 2^n, не включая n
print(output_list)

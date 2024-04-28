# Пользователь вводит 3 числа,
# сказать сколько из них положительных и сколько отрицательных

# ничего лучше в голову не пришло
user_input = input(
    "Введите три числа, разделяя их пробелами: ")
split_numbers = user_input.split(" ")
count_zero = user_input.count("-")

print(f"Вы ввели {(float(split_numbers[0]) > 0) + (float(split_numbers[1]) > 0) +
      (float(split_numbers[2]) > 0)} положительных числа и {(float(split_numbers[0]) < 0) +
      (float(split_numbers[1]) < 0) + (float(split_numbers[2]) < 0)} отрицательных числа.")

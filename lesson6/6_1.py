# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def convert_str_to_int(str_number):
    number = 0
    dict_number = {'0': 0, '1': 1, '2': 2, '3': 3,
                   '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for _ in range(0, len(str_number)):
        number = number + \
            (dict_number[str_number[len(str_number) - 1 - _]] * (10**(_)))


def dec_to_bin(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


def bin_to_dec(number):
    result = 0
    for _ in range(0, len(number)):
        result = result +


user_number = input(
    "Введите число в десятичной системе, для перевода в двоичную систему и обратно: ")
dec_number = convert_str_to_int(user_number)
print(f"Число {dec_number} в двойчном счислении: {dec_to_bin(dec_number)}")
bin_number = convert_str_to_int(dec_number)
print(f"Число {dec_number} в десятичном счислении: {bin_to_dec(bin_number)}")

# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def convert_str(str_number):
    number = 0
    dict_number = {'0': 0, '1': 1, '2': 2, '3': 3,
                   '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for _ in range(0, len(str_number)):
        number = number + \
            (dict_number[str_number[len(str_number) - 1 - _]] * (10 ** _))
    return number


def dec_to_bin(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


def bin_to_dec(number):
    result = 0
    power = 0
    while number > 0:
        result = result + (number - (number // 10) * 10) * (2 ** power)
        number = number // 10
        power += 1
    return result


user_number = input(
    "Введите число в десятичной системе, для перевода в двоичную систему и обратно: ")
dec_number = convert_str(user_number)
print(f"Число {dec_number} в двойчном исчислении: {dec_to_bin(dec_number)}")
bin_number = convert_str(dec_to_bin(dec_number))
print(f"Число {bin_number} в десятичном исчислении: {bin_to_dec(bin_number)}")

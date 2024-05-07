# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def reversing_list(some_list):
    for position in range(0, len(some_list) // 2):
        some_list[position], some_list[-(position + 1)] = \
            some_list[-(position + 1)], some_list[position]
    return some_list


some_list = [5, 45, -2, 1, 0]

print("Исходный список: ", some_list)
print("Развернутый список: ", reversing_list(some_list))

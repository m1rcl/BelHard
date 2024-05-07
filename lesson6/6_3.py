# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def shift_list(user_list, shift):
    output_list = []
    for _ in range(shift + 1, len(user_list)):
        output_list.append(user_list[_])
    for _ in range(0, shift + 1):
        output_list.append(user_list[_])
    return output_list


user_list = [1, 2, 3, 4, 5, 6, 7]
shift = int(input("Введите позицию сдвига списка: "))
print("Результат свдига:", shift_list(user_list, shift))

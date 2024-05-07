# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

def filtering_list(some_list):
    odd_list = []
    even_list = []
    for _ in some_list:
        if _ % 2:
            odd_list.append(_)
        else:
            even_list.append(_)
    return even_list + odd_list


some_list = [4, 7, 34, 67, 23, 0, 5]

print("Исходный список: ", some_list)
print("Отфильтрованный список: ", filtering_list(some_list))

# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

def count_list(some_list):
    output_list = []
    for _ in range(0, len(some_list) - 1):
        output_list.append(some_list[_ - 1] + some_list[_ + 1])
    output_list.append(some_list[-2] + some_list[0])
    return output_list


some_list = [5, 45, -2, 1, 0]

print("Исходный список: ", some_list)
print("Посчитанный список: ", count_list(some_list))

# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

def count_list(some_list):
    output_list = []
    for _ in range(0, len(some_list)):
        print(some_list[_ - 1], some_list[_],
              some_list[(len(some_list) + 1) - (len(some_list) - _)])
        sum_numbers = some_list[_ - 1] + some_list[_] + \
            some_list[(len(some_list) + _) - len(some_list)]
        output_list.append(sum_numbers)
    return output_list


some_list = [5, 45, -2, 1, 0]

print("Исходный список: ", some_list)
print("Посчитанный список: ", count_list(some_list))

# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

def filtering_list(in_list):
    if isinstance(in_list, str):
        return True
    else:
        return False


some_list = ['hello', True,  [], 10, "my name is", 0]

print("Исходный список: ", some_list)
print("Отфильтрованный список: ", list(filter(filtering_list, some_list)))

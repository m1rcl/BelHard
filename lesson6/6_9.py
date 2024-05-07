# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users_data = {
    1: {
        "first name": "Ivan",
        "last name": "Ivanov",
        "email": "ivan_ivanov@gmail.com"},
    2: {
        "first name": "Petr",
        "last name": "Petrov",
        "email": ""},
    3: {
        "first name": "Alexey",
        "last name": "Alexeev", }
}

print("Элетронная почта следующих пользователей не известна:")
for _ in range(1, len(users_data) + 1):
    if "email" not in users_data[_].keys() or not users_data[_]["email"]:
        print(users_data[_]["first name"], users_data[_]["last name"])

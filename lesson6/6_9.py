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
for user_id in users_data:
    if "email" not in users_data[user_id].keys() or not users_data[user_id]["email"]:
        print(users_data[user_id].get("first name"),
              users_data[user_id].get("last name"))

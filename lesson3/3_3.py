# Пользователь вводит Имя, Возраст и Город,
# сформировать приветственное сообщение путем форматирования 3-мя способами

USER_NAME = input("Введите ваше имя: ")
USER_AGE = input("Введите ваш возраст: ")
USER_CITY = input("Введите ваш город: ")

print("Здравствуйте, %s. Вы прожили все %s лет в городе %s?" %
      (USER_NAME, USER_AGE, USER_CITY))

print("Здравствуйте, {name}. Вы прожили все {age} лет в городе {city}?".format(
    name=USER_NAME, age=USER_AGE, city=USER_CITY))

print(f"Здравствуйте, {USER_NAME}. Вы прожили все {
      USER_AGE} лет в городе {USER_CITY}?")

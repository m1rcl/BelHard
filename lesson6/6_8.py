# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

def country_identificating(user_input):
    city_dict = {"England": ["London", "Manchester", "York"], "France": ["Paris", "Orlean", "Lionne"],
                 "Russia": ["Moscow", "St. Peterburg", "Smolensk"], "Belarus": ["Minsk", "Brest", "Mogilev"]}
    for (country, cities) in city_dict.items():
        if user_input in cities:
            return country
    else:
        return "неизвестной стране"


user_input = input("Введите название города: ")
print(f"{user_input} находится в {country_identificating(user_input)}")

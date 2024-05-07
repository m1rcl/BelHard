# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

def country_identificating(user_input):
    city_dict = {"England": "London", "France": "Paris",
                 "Russia": "Moscow", "Belarus": "Minsk"}
    for (country, city) in city_dict.items():
        # for country, city in city_dict.items():
        if user_input == city:
            return country
    else:
        return "неизвестного государства"


user_input = input("Введите название столицы: ")
print(f"{user_input} столица {country_identificating(user_input)}")

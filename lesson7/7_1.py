# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

class Car():

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy: bool = False

    def __str__(self):
        return f"color: {self.color}, passenger seats: {self.count_passenger_seats}, baby seat: {self.is_baby_seat}"


my_car1 = Car(color="black", count_passenger_seats=4, is_baby_seat=False)
print(my_car1)
my_car2 = Car(color="white", count_passenger_seats=5, is_baby_seat=True)
print(my_car2)

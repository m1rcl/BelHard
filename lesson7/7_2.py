# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

class Car():

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy: bool = False

    def __str__(self):
        return f"color: {self.color}, passenger seats: {
            self.count_passenger_seats}, baby seat: {self.is_baby_seat}"


class Taxi():

    def __init__(self, cars: list):
        self.cars = cars

    def find_car(self, count_passenger_seats: int, is_baby_seat: bool):
        for car in self.cars:
            if count_passenger_seats == car.count_passenger_seats \
                    and is_baby_seat == car.is_baby_seat and not car.is_busy:
                car.is_busy = True
                return car
        else:
            return None


my_car1 = Car(color="black", count_passenger_seats=4, is_baby_seat=False)
my_car2 = Car(color="white", count_passenger_seats=5, is_baby_seat=True)
taxi_available = Taxi([my_car1, my_car2])

print(taxi_available.find_car(count_passenger_seats=4, is_baby_seat=False))

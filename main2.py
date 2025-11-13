# Тема:Наследование
#     инкапсуляция - изолирует объект
#     public - публичный
#     _protected - защищены
#     __private- приватный

class Animal:#родительский класс
    def __init__(self, name , age, color, gender):
        self.name = name 
        self.__age = age 
        self.color = color 
        self.gender = gender
        # @property  Декораторы
    def age(self):
        return self.__age
    
    # @age.setter
    def age(self, value):
        if value >0 and value < 20:
            self.__age = value

    
    def info(self):
        print(f" Информация о животном ")
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.__age} лет")
        print(f"Имя: {self. color }")

    def set_name(self, new_name):# изменение имени
        old_name = self.name
        self.name = new_name
        print(f"Имя изменено: {old_name} ➜ {self.name}")


class Cat(Animal): #наследование/ дочерний класс Animal'a
    def mau(self):
        print("мяу-мяу")

class Dog(Animal): #наследование/ дочерний класс Animal'a
    def gav(self):
        print("гав-гав")


cat1 = Cat("Felix", 2, "Рыжий", "самка")
dog1 = Dog("Bobik", 2, "черный", "самец")
cat1.age = 12
# print(cat1.age)

# 
# 
# 
# cat1.set_name("Gena")  # меняем имя
# dog1.set_name("Sharik")  # меняем имя собаки
# dog1.info()  # выводим информацию о собаке
# cat1.info()  ## выводим информацию о кошке
# cat1.mau()
# dog1.gav()



#Магазин с наследованием
# Базовый класс Product
# Общие атрибуты дял всех товаров :
# name- название товара
# price - цена
# quantity - количество товара на складе
# Методы:
# buy(amount) - уменьашет количество товара во время покупки, если хватает на складе
# show_info() - выводит иформацию о товаре


# Класс FoodProduct (наследник Product)
# Доп атрибут: expiration_date - срок годности
# Доп метод: show_expiration() - выводит срок годности товара

# Класс ElectronicsProduct (наследник Product)
# Доп. атрибут : warranty_years - гарантия в годах
# Доп метод: show_warranty() - выводит срок гарантии


# Базовый класс Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Куплено {amount} шт. товара '{self.name}'. Осталось: {self.quantity}")
        else:
            print(f"Недостаточно товара '{self.name}' на складе!")

    def show_info(self):
        print(f"Название: {self.name}, Цена: {self.price} сом., Количество: {self.quantity}")


# Класс FoodProduct
class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date): #доп атрибут
        super().__init__(name, price, quantity)  # super() используется в классах-наследниках, чтобы обратиться к методам (или атрибутам) родительского класса.
        self.expiration_date = expiration_date

    def show_expiration(self):
        print(f"Срок годности: {self.expiration_date}")


# Класс ElectronicsProduct
class ElectronicsProduct(Product):
    def __init__(self, name, price, quantity, warranty_years):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    def show_warranty(self):
        print(f"Гарантия: {self.warranty_years} года(лет)")



apple = FoodProduct("Яблоко", 50, 20, "2025-12-01")
laptop = ElectronicsProduct("Ноутбук", 85000, 5, 2)

# apple.show_info()
# apple.show_expiration()
# apple.buy(3)
# print()

laptop.show_info()
laptop.show_warranty()
laptop.buy(1)


# Задача Банковский счёт с инкапсуляцией
# Создай класс BankAccount, который моделирует банковский счёт.

# Атрибуты приватные:

#  __owner — владелец счёта

#  __pin_code — пин-код (задаётся при создании)

#  __balance — баланс (по умолчанию 0)



# Методы:

#  1. get_balance(pin) — возвращает баланс, если пин-код правильный

#  2. депозит(деньги) — пополнение счёта (не требует пин-кода)

#  3. снять(деньги, pin) — снимает деньги, если хватает средств и пин-код правильный

#  4. Change_pin(old_pin, new_pin) — смена пин-кода (проверяет старый пин)

#  5. info() — выводит имя владельца и «закрытый» баланс (например, «Баланс: **** сом»)


class BankAccount:
    def __init__(self, owner, pin_code):
        self.__owner = owner
        self.__pin_code = pin_code
        self.__balance = 0

    def get_balance(self, pin):    #Возвращает баланс, если пин-код верный
        if pin == self.__pin_code:
            return f"Ваш баланс: {self.__balance} сом"
        else:
            return "неверный пин-код!"

    def deposit(self, amount): #Пополнение счёта
        if amount > 0:
            self.__balance += amount
            return f"Счёт пополнен на {amount} сом. Текущий баланс: {self.__balance} сом"
        else:
            return "Сумма должна быть положительной!"

    def withdraw(self, amount, pin):  #Снятие денег
        if pin != self.__pin_code:
            return "неверный пин-код!"
        if amount > self.__balance:
            return "Недостаточно средств!"
        self.__balance -= amount
        return f"Вы сняли {amount} сом. Остаток: {self.__balance} сом"

    def change_pin(self, old_pin, new_pin):  #Смена пин-кода
        if old_pin == self.__pin_code:
            self.__pin_code = new_pin
            return "Пин-код успешно изменён!"
        else:
            return "Ошибка: старый пин-код неверен!"

    def info(self):  #Информация о владельце и скрытом балансе
        return f"Владелец: {self.__owner}, Баланс: **** сом"


acc = BankAccount("Малика", 1500)
# print(acc.info())
# print(acc.deposit(5000))
# print(acc.get_balance(1234))
# print(acc.withdraw(2000, 1234)) #снятие
# print(acc.change_pin(1234, 4321))
# print(acc.get_balance(4321))


# Задача: Система авиабронирования
# Создай программу, используй классы, инкапсуляцию и взаимодействие объектов.
# Программа должна позволять: добавлять и удалять рейсы, покупать и отменять билеты, изменять параметры рейса, рассчитывать общую выручку, показывать статистику.
# Класс Flight: Отвечает за конкретный рейс. Содержит: направление (route), количество мест эконом и бизнес, цены,количество проданных билетов,методы для продажи, отмены и изменения данных.
# Класс Airline: Управляет всеми рейсами: список (или словарь) всех рейсов, методы добавления, удаления, поиска и статистики.
# Класс Client, Сохраняет данные клиента и купленного билета.

class Flight:
    def __init__(self, flight_number: str, route: str, seats_economy: int, seats_business: int,
                 price_economy: float, price_business: float):#Номер рейса содержит буквы и цифры, поэтому строка, а не число
        #int — целое число   Количество мест — это всегда целое число
        #float — число с плавающей точкой
        self.flight_number = flight_number
        self.route = route #направление
        self._seats_economy = seats_economy
        self._seats_business = seats_business
        self._price_economy = price_economy
        self._price_business = price_business
        self._sold_economy = 0
        self._sold_business = 0

    # Методы для продажи и отмены билета
    def sell_ticket(self, seat_type: str) -> bool:#-> bool — подсказка, что метод возвращает логическое значение (True или False):
        if seat_type == "economy" and self._sold_economy < self._seats_economy:
            self._sold_economy += 1
            return True
        elif seat_type == "business" and self._sold_business < self._seats_business:
            self._sold_business += 1
            return True
        else:
            return False

    def cancel_ticket(self, seat_type: str) -> bool:
        if seat_type == "economy" and self._sold_economy > 0:
            self._sold_economy -= 1
            return True
        elif seat_type == "business" and self._sold_business > 0:
            self._sold_business -= 1
            return True
        else:
            return False

    # Методы для изменения параметров
    def update_prices(self, new_price_economy: float, new_price_business: float):
        self._price_economy = new_price_economy
        self._price_business = new_price_business

    def update_route(self, new_route: str):
        self.route = new_route

    # Расчет выручки
    def revenue(self) -> float:
        return self._sold_economy * self._price_economy + self._sold_business * self._price_business

    # Статистика по рейсу
    def get_info(self) -> str:
        return (f"Рейс {self.flight_number} ({self.route})\n"
                f"Эконом: {self._sold_economy}/{self._seats_economy} продано по {self._price_economy}сом\n"
                f"Бизнес: {self._sold_business}/{self._seats_business} продано по {self._price_business}сом\n"
                f"Выручка: {self.revenue()}сом\n")


class Client:
    def __init__(self, name: str, passport: str):
        self.name = name
        self.passport = passport
        self.tickets = []  # список кортежей (flight_number, seat_type)

    def buy_ticket(self, flight: Flight, seat_type: str):
        if flight.sell_ticket(seat_type):
            self.tickets.append((flight.flight_number, seat_type))
            print(f"{self.name} купил билет на рейс {flight.flight_number} ({seat_type})")
        else:
            print(f"Билетов {seat_type} нет на рейс {flight.flight_number}")

    def cancel_ticket(self, flight: Flight, seat_type: str):
        if (flight.flight_number, seat_type) in self.tickets and flight.cancel_ticket(seat_type):
            self.tickets.remove((flight.flight_number, seat_type))
            print(f"{self.name} отменил билет на рейс {flight.flight_number}")
        else:
            print("Ошибка отмены: билет не найден или не может быть отменён.")


class Airline:
    def __init__(self, name: str):
        self.name = name
        self._flights = {}

    # Управление рейсами
    def add_flight(self, flight: Flight):
        if flight.flight_number not in self._flights:
            self._flights[flight.flight_number] = flight
            print(f"Добавлен рейс {flight.flight_number} ({flight.route})")
        else:
            print("Рейс с таким номером уже существует!")

    def remove_flight(self, flight_number: str):
        if flight_number in self._flights:
            del self._flights[flight_number]
            print(f"Рейс {flight_number} удалён.")
        else:
            print("Рейс не найден.")

    def find_flight(self, flight_number: str) -> Flight:
        return self._flights.get(flight_number, None)

    def total_revenue(self) -> float:
        return sum(f.revenue() for f in self._flights.values())

    def show_statistics(self):
        print(f"\nАвиакомпания {self.name} — статистика рейсов:")
        for flight in self._flights.values():
            print(flight.get_info())
        print(f"Общая выручка: {self.total_revenue()}сом\n")


# ======= Пример использования =======
if __name__ == "__main__":
    airline = Airline("SkyWings")

    # Создаём рейсы
    f1 = Flight("SW101", "Москва - Париж", 10000, 10, 1500.0, 500.0)
    f2 = Flight("SW202", "Москва - Лондон", 12000, 12, 1700.0, 550.0)

    # Добавляем рейсы
    airline.add_flight(f1)
    airline.add_flight(f2)

    # Создаём клиентов
    c1 = Client("Айчурок Ормонова", "123456789")
    c2 = Client("Малика Акылбекова", "987654321")

    # Покупка билетов
    c1.buy_ticket(f1, "economy")
    c1.buy_ticket(f1, "business")
    c2.buy_ticket(f2, "economy")

    # Отмена билета
    c1.cancel_ticket(f1, "economy")

    # Изменение цены и маршрута
    f1.update_prices(16000.0, 5200.0)
    f2.update_route("Жалал-Абад - Италия (через Турцию)")

    # Статистика
    airline.show_statistics()

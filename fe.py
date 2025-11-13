# 1. Класс Tour 
# Каждый тур имеет свою цену, длительность, статус (доступен/забронирован) и клиента, который его купил.
# Клиенты могут просматривать доступные туры, бронировать и оплачивать их.
# Агентство может смотреть общую выручку и управлять турами.

# 1. Класс Tour
# Инкапсулированный класс, представляющий один тур.
# Атрибуты:
# __id — уникальный номер тура (инкапсулированный, доступ только через свойство);
# __price — цена тура (инкапсулированный, управляется через @property);
# _is_booked — защищённый атрибут (True/False);
# _client — текущий клиент или None;
# _days — количество дней тура.

# Методы:
# book(client) — бронирует тур, делает его недоступным, если клиент оплатил.
# cancel_booking() — отменяет бронь, делает тур доступным.
# info() — краткая информация о туре.

# Свойства:
# price — через @property и @setter (цена не может быть ниже 5000 сом).
# id — только для чтения.

# 2. Класс Client
# Атрибуты:
# name — имя клиента;
# balance — баланс клиента.

# Методы:
# pay(amount) — уменьшает баланс, если хватает денег;
# add_balance(amount) — пополнение счёта;
# info() — возвращает строку с именем и балансом.


# 3. Класс Agency
# Атрибуты:
# name — название агентства;
# tours — список объектов Tour;
# _income — защищённый атрибут (доход агентства).

# Методы:
# add_tour(tour) — добавляет новый тур;
# show_available_tours() — показывает все свободные туры;
# book_tour(client, tour_id) — бронирует тур для клиента;
# cancel_all_bookings() — отменяет все активные брони;
# show_status() — показывает состояние всех туров и текущую выручку. 

class Tour:
    def __init__(self, id, price, days):
        self.__id = id   ## уникальный номер тура
        self.__price = price ## цена тура
        self._is_booked = False  ## тур забронирован или нет
        self._client = None # кто купил тур
        self._days = days  # длительность тура
    
    @property
    def id(self):
        return self.__id
    
    @property #Свойства-позволяют обращаться к функции как к обычной переменной,но при этом можно добавить логику
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value>=5000:
            self.__price = value
        else:
            print("цена не может быть ниже 5000 сом")


    def book(self, client): #бронирует тур, делает его недоступным
         # если тур свободен и клиент оплатил
        if not self._is_booked and client.pay(self.__price):
            self._is_booked = True
            self._client = client
            return True
        return False

    def cancel_booking(self): #отменяет бронь, делает тур доступным
        self._is_booked = False
        self._client = None 

    def info(self): 
        status = "Забронирован" if self._is_booked else "Доступен"
        client_name = self._client.name if self._client else "-"
        return f"Тур №{self.__id}: {self.__price} сом, {self._days} дней, {status}, клиент: {client_name}"
    
class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print(f"{self.name}, недостаточно денег для оплаты тура")
            return False

    def add_balance(self, amount):
        self.balance += amount

    def info(self):
        return f"{self.name}, баланс: {self.balance} сом"


class Agency:
    def __init__(self, name):
        self.name = name 
        self.tours = [] 
        self._income = 0  #доход агентства
    def add_tour(self, tour): #добавляет новый тур;
        self.tours.append(tour)
    def show_available_tours(self): # показывает все свободные туры;
        for t in self.tours:
            if not t._is_booked:
                print(t.info())
    def book_tour(self, client, tour_id): #бронирует тур для клиента;
        for t in self.tours:
            if t.id == tour_id and not t._is_booked:
                if t.book(client):
                    self._income += t.price
                    print(f"{client.name} забронировал тур №{tour_id}")
                return
        print("Тур недоступен или не найден")
    def cancel_all_bookings(self): #отменяет все активные брони;
        for t in self.tours:
            t.cancel_booking()

    def show_status(self): #показывает состояние всех туров и текущую выручку.
        print(f"Агентство: {self.name}, доход: {self._income} сом")
        for t in self.tours:
            print(t.info())
 
# создаём агентство
a1 = Agency("Malika Travel")
# создаём туры
t1 = Tour(1, 10000, 5)
t2 = Tour(2, 15000, 7)
# добавляем туры в агентство
a1.add_tour(t1)
a1.add_tour(t2)
# создаём клиента
c1 = Client("Алия", 20000)
# показываем доступные туры
print("\nСвободные туры:")
a1.show_available_tours()
# бронируем тур
a1.book_tour(c1, 1)
# проверяем статус агентства
print("\nСтатус агентства:")
a1.show_status()
# отменяем все брони
a1.cancel_all_bookings()
# снова проверяем статус
print("\nПосле отмены всех броней:")
a1.show_status()


#agency income — доход агентства





# Задача Симуляция компьютерного клуба
# создаём систему для комп клуба, где можно бронировать и оплачивать места.
# Каждый компьютер имеет свою цену за час, статус (свободен/занят), и время, когда его забронировали.
# Клиенты могут садиться за компьютер, играть и оплачивать время.
# Владелец клуба может смотреть выручку и управлять компьютерами.

# 1. класс Computer
# Инкапсулированный класс, представляющий компьютер.
# Атрибуты:
# __id — уникальный номер (инкапсулированный, доступ через свойство).
# __hourly_rate — цена за час (инкапсулированный, управляется через @property).
# _is_busy — защищённый атрибут (True/False).
# _current_client — текущий клиент или None.
# _start_time — время начала сессии.
# Методы:
# start_session(client, hours) — запускает сессию, делает компьютер занятым.
# end_session() — завершает сессию, считает оплату.
# info() — краткое состояние компьютера.
# Свойства:
# hourly_rate — с @property и @setter: цена не может быть ниже 50 сом.
# id — только для чтения (@property, без setter).

# 2. Client
# Атрибуты: name, balance
# Методы:
# pay(amount) — уменьшает баланс, если хватает денег.
# add_balance(amount) — пополнение счёта.
# info() — информация о клиенте.

# 3. Club
# Атрибуты: name, computers — список объектов Computer
# _income — защищённый атрибут, выручка клуба.
# Методы:
# add_computer(computer)
# find_free_computer()
# serve_client(client, hours) — находит свободный комп, запускает сессию.
# end_all_sessions() — завершает все активные сессии и увеличивает доход клуба.
# show_status() — показывает состояние всех компьютеров и доход.



class Computer:
    def __init__(self, comp_id, hourly_rate):
        self.__id = comp_id                 # инкапсулированный id
        self.__hourly_rate = max(50, hourly_rate)  # цена за час, минимум 50
        self._is_busy = False               # занят или свободен
        self._current_client = None         # имя клиента
        self._start_time = None             # время начала сессии

    @property    #Это специальные методы, чтобы красиво обращаться к скрытым данным.
    def id(self):
        return self.__id

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value >= 50:
            self.__hourly_rate = value  ## создаём компьютеры


    def start_session(self, client, hours):
       if not self._is_busy:
            self._is_busy = True
            self._current_client = client
            self._start_time = hours
            print(f"{client} начал игру на {hours} ч.")

    def end_session(self):
        if self._is_busy:
            payment = self._start_time * self.__hourly_rate
            print(f"С {self._current_client} к оплате {payment} сом.")
            self._is_busy = False
            self._current_client = None
            self._start_time = None
            return payment

    def info(self):
        status = "Занят" if self._is_busy else "Свободен"
        return f"ПК {self.__id}: {status}, {self.__hourly_rate} сом/час"

# pc1 = Computer(1, 80)
# print(pc1.info())          # ПК 1: Свободен, 80 сом/час
# pc1.start_session("Иван", 2)
# pc1.end_session()          # С Малика к оплате 160 сом.
# print(pc1.info())          # ПК 1: Свободен, 80 сом/час



class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        """Оплата услуги, если хватает денег"""
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} оплатил {amount} сом. Остаток: {self.balance} сом.")
            return True
        else:
            print(f"Недостаточно средств у {self.name}. Нужно {amount}, есть {self.balance}.")
            return False

    def add_balance(self, amount):
        """Пополнение счёта"""
        self.balance += amount
        print(f"{self.name} пополнил счёт на {amount} сом. Баланс: {self.balance} сом.")

    def info(self):
        """Информация о клиенте"""
        return f"Клиент: {self.name}, баланс: {self.balance} сом"

# client1 = Client("Азамат", 500)
# print(client1.info())

# client1.pay(200)
# client1.add_balance(100)
# print(client1.info())


class Club:
    def __init__(self, name):
        self.name = name
        self.computers = []     # список компьютеров
        self._income = 0        # выручка клуба

    def add_computer(self, computer):
        self.computers.append(computer)

    def find_free_computer(self):
        """Находит первый свободный компьютер"""
        for comp in self.computers:
            if not comp._is_busy:
                return comp
        return None

    def serve_client(self, client, hours):
        """Посадить клиента за свободный компьютер"""
        comp = self.find_free_computer()
        if comp:
            cost = comp.hourly_rate * hours
            if client.pay(cost):
                comp.start_session(client.name, hours)
                self._income += cost
            else:
                print(f"{client.name} не смог оплатить сессию.")
        else:
            print("Нет свободных компьютеров.")

    def end_all_sessions(self):
        """Завершает все активные сессии"""
        for comp in self.computers:
            if comp._is_busy:
                comp.end_session()

    def show_status(self):
        """Показывает состояние всех компьютеров и выручку"""
        print(f"\nКлуб: {self.name}")
        for comp in self.computers:
            print(comp.info())
        print(f"Выручка клуба: {self._income} сом\n")
# создаём компьютеры
pc1 = Computer(1, 60)
pc2 = Computer(2, 80)

# создаём клиентов
client1 = Client("Азамат", 500)
client2 = Client("Дина", 200)

# создаём клуб
club = Club("CyberX")

club.add_computer(pc1)
club.add_computer(pc2)

# клиенты садятся за компьютеры
club.serve_client(client1, 2)   # Азамат 2 часа
club.serve_client(client2, 3)   # Дина 3 часа

club.show_status()

# завершаем все сессии
club.end_all_sessions()
club.show_status()

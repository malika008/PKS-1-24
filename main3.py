# "Симуляция банка" — создать модель банка, где клиенты могут:
# открывать депозиты, брать кредиты, оформлять рассрочки на товары.
# Банк должен уметь учитывать эти операции и подсчитывать свою прибыль.

# 1. класс Person
# Атрибуты: name, age, balance
# Методы: deposit(amount) — пополнение счёта.
# withdraw(amount) — снятие со счёта.
# info() — возвращает краткую информацию о клиенте.

# 2. класс Bank
# Атрибуты: name, clients — список объектов Person, products — список активных продуктов
# (депозиты, кредиты, рассрочки), 
# income — доход банка
# Методы: add_client(client), add_product(product)
# calculate_total_profit() — суммирует доходы по всем продуктам.

# 3. класс BankProduct (базовый класс)
# Атрибуты: client, amount, interest_rate, term_months
#методы : calculate_interest(), - рассчитывает сумму процентов
# info() - краткая инофрмация о продукте 

# 4. класс Deposit ( наследник BankProduct)
# Деньги клитента передаются банку и по окончанит срока клеиент получает сумму+проценты.
#метод close_deposit() возвращает клиенту деньги и начисление проценты

#5 класс Credit (наследнки BankProduct)
# банк выдаёт клиенту деньги, которые тот должен вернуть с процентами 
#Метод monthly_payment() рассчитывает ежемесячный плтаёэ по кредиту
# метод close_credit() возвращет банку тело кредита и поценты (уменьшает баланс клиента)

#6. класс Installment (Рассрочка)
# Клиент покупает товар в рассрочку (без процентов, но с комиссией).
# Атрибуты: product_name, commission_rate
# Методы: monthly_payment(), close_installment() 







class Person:
    def __init__(self, name, age, balance=0):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):   # — снятие со счёта.
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} снятие со счёта {amount}")
        else:
            print("Недостаточно средств!")

    def info(self):
        return f"{self.name}, {self.age} лет, баланс: {self.balance} сом."


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.products = []  # список всех операций
        self.income = 0  #доход

    def add_client(self, client):
        self.clients.append(client)
        print(f"Клиент {client.name} добавлен")

    def add_product(self, product):
        self.products.append(product)
        print(f"Продукт добавлен")

    def add_income(self, amount):
        self.income += amount 

    def calculate_total_profit(self):
        return self.income
    
    def show_clients(self):
        print("Наши клиенты:")
        for c in self.clients:
            print(f".   {c.info()}")
    def show_product(self):
        print("Наши продукты:")
        for c in self.products:
            print(f".   {c.info()}")


class BankProduct:
    def __init__(self, client, amount, interest_rate, term_months):
        self.client = client              # объект клиента (Person)
        self.amount = amount              # сумма вклада или кредита
        self.interest_rate = interest_rate  # годовая процентная ставка
        self.term_months = term_months      # срок в месяцах

    def calculate_interest(self):
        """Рассчитать сумму процентов за весь срок."""
        # Формула: проценты = сумма * ставка * (месяцев / 12)
        interest = self.amount * (self.interest_rate / 100) * (self.term_months / 12)
        return interest

    def info(self):
        """Краткая информация о продукте."""
        return (f"Клиент: {self.client.name}, "
                f"Сумма: {self.amount} сом, "
                f"Ставка: {self.interest_rate}%, "
                f"Срок: {self.term_months} мес., "
                f"Проценты: {self.calculate_interest():.2f} сом.")
    
class Deposit(BankProduct):
    def __init__(self, client, amount, interest_rate, term_months):
        super().__init__(client, amount, interest_rate, term_months)
        # При открытии вклада деньги уходят со счёта клиента
        if client.balance >= amount:
            client.withdraw(amount)
            print(f"{client.name} открыл депозит на {amount} сом.")
        else:
            print("Недостаточно средств для открытия депозита!")

    def close_deposit(self):
        """Возвращает клиенту сумму + проценты"""
        total = self.amount + self.calculate_interest()
        self.client.deposit(total)
        print(f"{self.client.name} получил {total:.2f} сом (включая проценты).")

    def info(self):
        return (f"[Депозит] Клиент: {self.client.name}, "
                f"Сумма: {self.amount} сом, "
                f"Ставка: {self.interest_rate}%, "
                f"Срок: {self.term_months} мес.")
    
class Credit(BankProduct):
    def __init__(self, client, amount, interest_rate, term_months):
        super().__init__(client, amount, interest_rate, term_months)
        client.deposit(amount)
        print(f"{client.name} получил кредит на {amount} сом под {interest_rate}%.")

    def monthly_payment(self):
        total = self.amount + self.calculate_interest()
        return round(total / self.term_months, 2)

    def close_credit(self):
        total = self.amount + self.calculate_interest()
        if self.client.balance >= total:
            self.client.withdraw(total)
            print(f"{self.client.name} закрыл кредит, выплатив {total:.2f} сом.")
        else:
            print("Недостаточно средств для погашения кредита!")

    def info(self):
        return (f"[Кредит] Клиент: {self.client.name}, "
                f"Сумма: {self.amount} сом, "
                f"Ставка: {self.interest_rate}%, "
                f"Срок: {self.term_months} мес., "
                f"Платёж: {self.monthly_payment()} сом/мес.")

class Installment(BankProduct):  #(Рассрочка)
    def __init__(self, client, product_name, amount, commission_rate, term_months):
        super().__init__(client, amount, 0, term_months)
        self.product_name = product_name
        self.commission_rate = commission_rate
        client.deposit(amount)  # клиент получает товар на сумму
        print(f"{client.name} оформил рассрочку на '{product_name}' на {amount} сом.")

    def monthly_payment(self):
        total = self.amount + (self.amount * self.commission_rate / 100)
        return round(total / self.term_months, 2)

    def close_installment(self):
        total = self.amount + (self.amount * self.commission_rate / 100)
        if self.client.balance >= total:
            self.client.withdraw(total)
            print(f"{self.client.name} полностью выплатил рассрочку за '{self.product_name}'.")
        else:
            print("Недостаточно средств для закрытия рассрочки!")

    def info(self):
        return (f"[Рассрочка] Клиент: {self.client.name}, "
                f"Товар: {self.product_name}, "
                f"Сумма: {self.amount} сом, "
                f"Комиссия: {self.commission_rate}%, "
                f"Срок: {self.term_months} мес., "
                f"Платёж: {self.monthly_payment()} сом/мес.")

    




    

bank = Bank("Банк Добро")

alice = Person("Алиса", 30, 100000)
bob = Person("Боб", 40, 50000)
bank.add_client(alice)
bank.add_client(bob)



print("\n--- Клиенты ---")
print(alice.info())
print(bob.info())

print("\n--- Прибыль банка ---")
print(f"Общая прибыль: {bank.calculate_total_profit()} сом.")
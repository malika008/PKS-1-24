# Создай три класса:
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if  amount > self.quantity:
            print(f"Недостаточно {self.name}")
            return False
        self.quantity -= amount
        print(f"Покупка {amount} шт {self.name} оформлен ")
        return True
    
    def info(self):
         print(f"{self.name} - {self.price}сом, осталось: {self.quantity}")
class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def buy_product(self, product, amount):
        total= product.price*amount
        if total<= self.balance:
            print("Недостаточно средств")
            return
        if not product.buy(amount):
            return
        self.balance -= total
        print(f"{self.name} купил {amount} товаров на сумму {total}.")

    def info(self):
        print(f"Покупатель: {self.name}, Баланс: {self.balance}")



class Store:
    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Товар {product.name} добавлен в магазин.")

    def show_products(self):
        print("Товары в магазине:")
        for prod in self.products:
            prod.info()

store = Store("Молочная лавка")
milk = Product("Молоко", 120,10)
chocolate = Product("Шоколад", 330,10)
bread = Product("Хлеб", 30, 8)
store.add_product(milk)
store.add_product(chocolate)
store.add_product(bread)
store.show_products()



# class Store
#    хранит список товара
#    методы:
#    add_product(product) - добавляет товар
#    show_products() - показывает товар
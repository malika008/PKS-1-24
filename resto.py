# ЗАДАЧА: «Система управления рестораном»
# Требуется разработать систему моделирования работы ресторана, используя инкапсуляцию, наследование, полиморфизм, а также *args и **kwargs.

# Класс Ingredient:
# защищённые атрибуты: _name, _quantity (в граммах)
# приватный атрибут: __price_per_gram
# свойство price_per_gram (цена ≥ 0.1)
# метод cost(weight): возвращает стоимость weight граммов

# Класс Dish (базовый класс для всех блюд):
# защищённые атрибуты: _name, _ingredients (словарь: ингредиент → граммы)
# приватный атрибут: __base_price (минимум 20 сом, через свойство)
# метод total_cost(): стоимость ингредиентов + base_price
# метод info(): будет переопределён в наследниках

# Наследники Dish:
# • HotDish — горячее блюдо
# Доп. атрибут: _spicy_level (0–5)
# info(): «Горячее блюдо: <name>, острота <spicy>, цена <total_cost>»
# • Dessert — десерт
# Доп. атрибут: _sweetness (0–10)
# info(): «Десерт: <name>, сладость <sweetness>, цена <total_cost>»
# • Drink — напиток
# Доп. атрибут: _volume_ml
# info(): «Напиток: <name>, объем <volume> мл, цена <total_cost>»

# Класс Kitchen:
# защищённый список _dishes
# метод add_dishes(*dishes): принимает любое количество блюд
# метод find_dishes(**filters): поиск по любым параметрам (name, spicy_level, sweetness и т.д.)
# метод remove_dish(dish)
# метод all_dishes(): возврат копии списка

# Класс Restaurant:
# атрибут name
# объект kitchen
# приватный атрибут __income (через свойство только чтение)
# метод order_dish(dish_name): продаёт блюдо, увеличивает доход, убирает из меню
# метод menu(): список всех блюд через info()
# метод status(): доход и количество оставшихся блюд 

class Ingredient:
     def __init__(self, name, quantity, price_per_gram):
        self._name = name
        self._quantity = quantity
        self.__price_per_gram = None
        self.price_per_gram = price_per_gram

     @property
     def price_per_gram(self):
        return self.__price_per_gram
     
     @price_per_gram.setter
     def price_per_gram(self, value):
        if value >= 0.1:
            self.__price_per_gram = value

     def cost(self, weight):
        return weight * self.__price_per_gram
class Dish:
    def __init__(self, name, ingredients, base_price):
        self._name = name
        self._ingredients = ingredients
        self._base_price = None
        self._base_price = base_price

    @property
    def base_price(self):
        return self.__base_price
    @base_price.setter
    def base_price(self, value):
        if value >= 20:
            self.__base_price = value
    def total_cost(self):
        return sum(ing.cost(w) for ing, w in self._ingredients.items()) + self.__base_price

    def info(self):
        return f"Блюдо: {self._name}, цена {self.total_cost()}"
    
class HotDish(Dish):
    def __init__(self, name, ingredients, base_price, spicy_level):
        super().__init__(name, ingredients, base_price)
        self._spicy_level = spicy_level

    def info(self):
        return f"Горячее блюдо: {self._name}, острота {self._spicy_level}, цена {self.total_cost()}"
class Dessert(Dish):
    def __init__(self, name, ingredients, base_price, sweetness):
        super().__init__(name, ingredients, base_price)
        self._sweetness = sweetness

    def info(self):
        return f"Напиток: {self._name}, объем {self._volume_ml} мл, цена {self.total_cost()}"
    
class Drink(Dish):
    def __init__(self, name, ingredients, base_price, volume_ml):
        super().__init__(name, ingredients, base_price)
        self._volume_ml = volume_ml

    def info(self):
        return f"Напиток: {self._name}, объем {self._volume_ml} мл, цена {self.total_cost()}"


class Kitchen:
    def __init__(self):
        self._dishes = []

    def add_dishes(self, *dishes):
        for d in dishes:
            self._dishes.append(d)

    def find_dishes(self, **filters):
        result = self._dishes
        for attr, value in filters.items():
            result = [d for d in result if getattr(d, f"_{attr}", None) == value]
        return result

    def remove_dish(self, dish):
        if dish in self._dishes:
            self._dishes.remove(d)

    def all_dishes(self):
        return list(self._dishes)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.kitchen = Kitchen()
        self.__income = 0

    @property
    def income(self):
        return self.__income

    def order_dish(self, dish_name):
        for d in self.kitchen.all_dishes():
            if d._name == dish_name:
                self.kitchen.remove_dish(d)
                self.__income += d.total_cost()
                return d
        return None

    def menu(self):
        return [d.info() for d in self.kitchen.all_dishes()]

    def status(self):
        return {"income": self.__income, "dishes_left": len(self.kitchen.all_dishes())}
    
   # ингредиенты
meat = Ingredient("Мясо", 5000, 0.5)
rice = Ingredient("Рис", 3000, 0.1)

# блюда
plov = HotDish("Плов", {meat: 150, rice: 100}, 50, 2)

# ресторан
rest = Restaurant("Ресторан")

# добавление блюда
rest.kitchen.add_dishes(plov)

# меню
print(rest.menu())

# заказ
rest.order_dish("Плов")

# статус
print(rest.status())


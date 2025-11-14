# ЗАДАЧА: Cистема книжного магазина
# Требуется реализовать систему управления книжным магазином с использованием инкапсуляции, наследования, аргументов *args и **kwargs.
# класс BaseBook:
# защищённые атрибуты: _title, _author
# приватный атрибут: __price
# свойство price с проверкой (цена ≥ 100)
# абстрактный метод info()
# Классы-наследники от BaseBook:
# • Book — обычная книга. Реализация info(): «Книга: <title> — <author>, <price> сом»
# • EBook — электронная книга. Доп. атрибут: _file_size_mb. info(): «Электронная книга: <title> — <author>, <price> сом, файл <size> МБ»
# • AudioBook — аудиокнига. Доп. атрибут: _duration_min. info(): «Аудиокнига: <title> — <author>, <price> сом, длительность <minutes> мин»
# Класс Inventory (склад):
# защищённый список _books
# метод add_books(*books): принимает любое количество объектов книг, проверяет тип
# метод find_books(**filters): возвращает список книг, соответствующих переданным параметрам
# метод remove_book(book): удаляет книгу
# метод all_books(): возвращает копию списка книг
# Класс BookStore:
# атрибут name
# объект inventory
# приватный атрибут __income + свойство income (только чтение)
# метод sell_book(title): ищет по названию, удаляет книгу, увеличивает доход
# метод show_status(): возвращает название магазина, доход и список всех книг через info()
# Требования:
# обязательно использовать инкапсуляцию (__ и _), наследование, полиморфизм, *args, **kwargs
# система должна демонстрировать добавление книг, поиск, продажу и отображение состояния магазина

from abc import ABC, abstractmethod

class BaseBook:
     def __init__(self, title, author, price):
        self._title = title  # защищённые атрибуты:
        self._author = author
        self.__price = None  # приватный атрибут:
        self.price = price 

     @property
     def price(self):
        return self.__price 
     @price.setter
     def price(self, value):
        if value>= 100:
            self.__price = value
        else:
            print("цена не может быть ниже 100 сом")

     @abstractmethod #Абстрактный метод — это шаблон, который говорит: “каждый дочерний класс обязан реализовать этот метод”.
     def info(self):
        return f"{self._title} {self._author} {self.__price}"
class Book(BaseBook):
    def info(self):
        return f"Книга: {self._title} — {self._author}, {self.price} сом"
    
class EBook(BaseBook):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self._file_size_mb = file_size_mb
    
def info(self):
        return (f"Электронная книга: {self._title} — {self._author}, "
                f"{self.price} сом, файл {self._file_size_mb} МБ")

class AudioBook(BaseBook):
    def __init__(self, title, author, price, duration_min):
        super().__init__(title, author, price)
        self._duration_min = duration_min

    def info(self):
        return (f"Аудиокнига: {self._title} — {self._author}, "
                f"{self.price} сом, длительность {self._duration_min} мин")
    
class Inventory:   #(склад)
    def __init__(self):
        self._books = []

    def add_books(self, *books):    #принимает любое количество объектов книг, проверяет тип
        for b in books:
            if isinstance(b, BaseBook):       # тип проверяем
                self._books.append(b)
    def find_books(self, **filters):    # возвращает список книг, соответствующих переданным параметрам
        result = self._books
        for attr, value in filters.items():
            result = [b for b in result if getattr(b, f"_{attr}", None) == value]
        return result
    def remove_book(self, book):  #удаляет книгу
        if book in self._books:
            self._books.remove(book)

    def all_books(self):  #возвращает копию списка книг
        return list(self._books)
    
class BookStore:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.__income = 0
    @property
    def income(self):
        return self.__income        # только чтение
    def sell_book(self, title):   #ищет по названию, удаляет книгу, увеличивает доход
        for b in self.inventory.all_books():
            if b._title == title:
                self.inventory.remove_book(b)
                self.__income += b.price
                return b
        return None
    def show_status(self):
        books_info = [b.info() for b in self.inventory.all_books()]
        return {
            "store": self.name,
            "income": self.__income,
            "books": books_info
        }
    
# Создаём простые книги
b1 = Book("Гарри Поттер", "Дж. Роулинг", 300)
b2 = Book("Властелин колец", "Дж. Толкин", 450)
b3 = Book("Маленький принц", "Антуан де Сент-Экзюпери", 200)

# Создаём магазин
store = BookStore("Книжный мир")

# Добавляем книги
store.inventory.add_books(b1, b2, b3)
print(store.show_status())
sold = store.sell_book("Гарри Поттер")
print("Продано:", sold.info())
print(store.show_status())

def fh():
    print("привет ребята")

hello = fh #это объект
hello()

###########
def gromko(text):
    return text.upper()

def tiho(text):
    return text.lower()
def speak(func, x):
    res = func(x)
    return res
print(speak(gromko, 'Как дела гена?'))
print(speak(tiho, 'Хорошо Вася сам как?'))
############
def inc(x):
    return x*2

def dec(x):
    return x/2
def oper(func, x):
    res = func(x)
    return res
print(oper(inc, 6))
print(oper(dec, 9))

########## декоратор - добавить новое поведение не изменяя код
def before_after(func):
    def wrapper():
        print("то что может работать до")
        func()
        print("то что может работать после")
    return wrapper
@before_after #там где собачка это декоратор
def say_hi():
    print("привет друг")
say_hi()

# decorated = before_after(say_hi)
# decorated()

########## @property
# Атрибут — это свойство (данные) объекта.
# Метод — это действие (функция), которое объект может выполнять.
# Название        Что делает             Когда вызывается
#  getter        получает значение       когда читаешь атрибут
# setter         задаёт новое значение   когда присваиваешь атрибуту что-то
# deleter        удаляет атрибут          когда вызываешь del

class Teacher:
    def __init__(self, name, phone):
        self.name = name
        self._phone = phone

    @property #мы обращаемся к методам как к атрибутам,хотя под капатом все
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self,value):
        print("Сеттер сработал")
        self._phone = value

    @phone.deleter
    def phone(self):
       print("Номер удалено!")
       del self._phone

    def info(self):
        return f"{self.name} {self._phone}"
    
t = Teacher('Ali', 770770770)
t.phone = 45
print(t.phone)
# del t.phone
print(t.info())


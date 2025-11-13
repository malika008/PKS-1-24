# *args - arguments
def add(*args):
    total = 0
    for i in args:
        total += i
    print(total)

add(4, 4, 4, 4, 4, 4, 7, 8)


#**kwargs - keyword arguments
def pets(owner, **kwargs):
    print (owner)
    for k,v in kwargs.items():
        print(k,v )

pets("Aliya", cat="Felix", dog="bObik", age=18)

##### комбинация
def demo(*args, **kwargs):
    print (args)
    print (kwargs)

demo(77777710101,180,90,name="Gena", prof="ckdnkd")
#######
class Student:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs

    def info(self):
        print(f"name: {self.name}")
        for i,v in self.kwargs.items():
            print(f"{i}:{v}")

s = Student("Oleg", age=20, prof="Engineer")
s.info()


my_str = " rgr4fef45ferfe567rgfrgr6789"
nums = []    #4,45,567.6789
num = ""

for ch in my_str:
    if ch.isdigit():  ##isdigit() — проверяет, цифра ли символ.
        num += ch #ch → значит «символ» (от слова character).
    else:
        if num != "":  # num — собирает цифры в одно число.
            nums.append(int(num))
            num = ""

if num != "":    # Когда встречаем букву, добавляем готовое число в nums.
    nums.append(int(num))  # В конце тоже добавляем, если число было последним.


print(nums)


import re####Регулярные выражения
nums = []    #4,45,567.6789
my_str = " rgr4fef45ferfe567rgfrgr6789"
numbers = re.findall(' [0-9]+', my_str)
for i in numbers:
    nums.append(int(i))
print(nums)









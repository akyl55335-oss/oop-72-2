# | Метод         | Что делает                |
# | ------------- | ------------------------- |
# | `__init__`    | конструктор               |
# | `__str__`     | вывод через `print()`     |
# | `__repr__`    | отображение объекта       |
# | `__len__`     | `len(obj)`                |
# | `__getitem__` | `obj[key]`                |
# | `__call__`    | вызов объекта как функции |
# | `__eq__`      | `==`                      |
# | `__lt__`      | `<`                       |
# | `__gt__`      | `>`                       |


# | Оператор | Магический метод | Пример   |
# | -------- | ---------------- | -------- |
# | `+`      | `__add__`        | `a + b`  |
# | `-`      | `__sub__`        | `a - b`  |
# | `*`      | `__mul__`        | `a * b`  |
# | `/`      | `__truediv__`    | `a / b`  |
# | `//`     | `__floordiv__`   | `a // b` |
# | `%`      | `__mod__`        | `a % b`  |


class Test:
    def __init__(self, value):
        self.value = value
    # print()
    def __str__(self):
        return self.value
    # +
    def __add__(self, other):
        return f"{self.value + other.value}"


test_obj = Test("Test text")
my_str = str("My text")

t_1 = Test(123)
t_2 = Test(321)
value_t = t_1 + t_2
# print(value_t)

# int_1 = 123
# int_2 = 321
# value_int = int_1 + int_2
# print(value_int)

# print(test_obj)
# print(my_str)


class Money:
    def __init__(self, sum_m, currency):
        self.sum_m = sum_m
        self.currency = currency
    def __add__(self, other):
        if self.currency == other.currency:
            return f"{self.sum_m + other.sum_m}"
        return "Разные валюты"


som = Money(100, "SOM")
usd = Money(100, "USD")

# sum_money = som + usd
# print(sum_money)

class Video:

    def __init__(self, content, title, descriptions):
        self.content = content
        self.title = title
        self.descriptions = descriptions
        self.view_count = 0

    def __call__(self, *args, **kwargs):
        self.view_count += 1
        print(self.view_count)



video_1 = Video("Test", "Title", "descriptions")
# video_1()
# video_1()
# video_1()

class BankAccount:
    # Атрибута класса
    bank_name = "Kompanion"
    bank_adres = "Krasnodarskaya"
    def __init__(self, login, first_name, last_name, balance=100, bonus=100):
        # Атрибуты объекта класса
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.bonus = bonus

    def just_method(self):
        pass
    @staticmethod
    def calculate_deposit():
        print("calculate_deposit")
    @classmethod
    def get_bank_name(cls):
        print(f"{cls.bank_name}")
    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"
    @property
    def total_balance(self):
        print(f"{self.login.value}")


ardager = BankAccount(t_1, "aradger", "kartanbekov")
arzy = BankAccount(t_2, "arybek", "abdyrakhmanov")
# ardager.calculate_deposit()
# BankAccount.calculate_deposit()
# BankAccount.get_bank_name()
# print(arzy.login)
# print(arzy.bank_name)
# print(ardager.login)
# print(ardager.bank_name)
# print(arzy.full_name)
print(arzy.total_balance)

if type(t_1) == type(ardager):
    print("Один и тот же класс")
else:
    print("разные классы")
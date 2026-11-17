# MageHero - mageHero
# mage_hero
class Hero:
    # конструктор класа NameClass()
    def __init__(self, name, lvl, hp):
        # Атрибуты экземпляра+|+объекта класса
        self.hero_name = name
        self.hero_lvl = lvl
        self.hero_hp = hp

    def action(self):
        print(f"{self.hero_name} base action")

kirito = Hero("Kir1to", 100, 1000)
asuna = Hero("Asuna", 101, 1001)
my_int = 123
my_str = "text"
# print(type(kirito))
# print(type(my_str))
# kirito.action()
# print(my_str.capitalize())
# print(kirito.hero_lvl)
# print(asuna.hero_lvl)
# kirito.action()
# asuna.action()

# Эта библиотека нужна для генерации фейковых (тестовых) данных:
# имён, адресов, email, телефонов и т.д. Она используется, когда нужно
# быстро заполнить программу или базу данных примерами без ручного ввода.
from faker import Faker

# Создаём генератор данных с русской локализацией
fake = Faker("ru_RU")

print("Сгенерированные пользователи:\n")

for i in range(1, 6):
    print(f"Пользователь №{i}")
    print("  Имя:     ", fake.name())
    print("  Email:   ", fake.email())
    print("  Телефон: ", fake.phone_number())
    print("  Адрес:   ", fake.address())
    print()
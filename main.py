# MageHero - mageHero
# mage_hero
# class Hero:
    # конструктор класа NameClass()
    # def __init__(self, name, lvl, hp):
    #     # Атрибуты экземпляра+|+объекта класса
    #     self.hero_name = name
    #     self.hero_lvl = lvl
    #     self.hero_hp = hp

#     def action(self):
#         print(f"{self.hero_name} base action")
#
# kirito = Hero("Kir1to", 100, 1000)
# asuna = Hero("Asuna", 101, 1001)
# my_int = 123
# my_str = "text"
# # print(type(kirito))
# # print(type(my_str))
# # kirito.action()
# # print(my_str.capitalize())
# # print(kirito.hero_lvl)
# # print(asuna.hero_lvl)
# # kirito.action()
# # asuna.action()
#
# # Эта библиотека нужна для генерации фейковых (тестовых) данных:
# # имён, адресов, email, телефонов и т.д. Она используется, когда нужно
# # быстро заполнить программу или базу данных примерами без ручного ввода.
# from faker import Faker
#
# # Создаём генератор данных с русской локализацией
# fake = Faker("ru_RU")
#
# print("Сгенерированные пользователи:\n")
#
# for i in range(1, 6):
#     print(f"Пользователь №{i}")
#     print("  Имя:     ", fake.name())
#     print("  Email:   ", fake.email())
#     print("  Телефон: ", fake.phone_number())
#     print("  Адрес:   ", fake.address())
#     print()
import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    price REAL
)
""")
conn.commit()


def create_book(title, author, price):
    cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (title, author, price))
    conn.commit()


def read_books():
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(row)


def update_book(id, price):
    cursor.execute("UPDATE books SET price = ? WHERE id = ?", (price, id))
    conn.commit()


def delete_book(id):
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()


create_book("Война и мир", "Лев Толстой", 850)
create_book("Мастер и Маргарита", "Михаил Булгаков", 700)
read_books()

update_book(1, 900)
delete_book(2)
read_books()


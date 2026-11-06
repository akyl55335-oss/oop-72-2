# Родительский класс
class Hero:
    # конструктор класа NameClass()
    def __init__(self, name, lvl, hp):
        # Атрибуты экземпляра+|+объекта класса
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        print(f"{self.name} base action")

# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def cast_spell(self):
        print(f"{self.name} cast fire bool")

    def action(self):
        print(f"Name: {self.name} lvl:{self.lvl}")



kirito = Hero("Kirito", 111, 11111)
gendalf = MageHero("gendalf", 100, 1000, 100)
gendalf_silver = MageHero("gendalf silver", 100, 1000, 100)

# kirito.action()
# gendalf.action()
# print(type(kirito))
# print(type(gendalf))
#
# print(kirito.name)
# print(gendalf.name)

class Fly:
    def action(self):
        print('Fly')
class Swim:
    def action(self):
        print('Swim')
class Animal(Fly, Swim):
    pass
    # def action(self):
    #     print('Action')

donald_duck = Animal()
# donald_duck.action()
# print(Animal.mro())
# donald_duck.swim()
# donald_duck.fly()

class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(A):
    def action(self):
        super().action()
        print("C")
class D(B, C):
    def action(self):
        super().action()
        print("D")

test_obj = D()
print(D.mro())
test_obj.action()
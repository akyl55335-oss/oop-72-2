from abc import ABC, abstractmethod


class Hero(ABC):

    def __init__(self, name: str, level: int, health: int, strength: int):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):

    def attack(self):
        print("Воин атакует мечом")


class Mage(Hero):

    def attack(self):
        print("Маг использует магию")


class Assassin(Hero):

    def attack(self):
        print("Ассасин атакует из-под тишка")


if __name__ == "__main__":
    warrior = Warrior("Артур", 10, 100, 25)
    mage = Mage("Гендальф", 15, 80, 30)
    assassin = Assassin("Альтаир", 12, 90, 20)

    for hero in [warrior, mage, assassin]:
        hero.greet()
        hero.attack()
        hero.rest()
        print()
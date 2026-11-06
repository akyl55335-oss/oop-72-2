from abc import ABC, abstractmethod


class Hero(ABC):

    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    @abstractmethod
    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):

    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):

    def __init__(self, name: str, lvl: int, hp: int, mp: int = 0):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:

    def __init__(self, hero: Hero, balance: float, password: str):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = "Simba"

    def login(self, password: str) -> bool:
        return self.__password == password

    @property
    def full_info(self) -> str:
        return f"Герой: {self.hero.name}, Класс: {type(self.hero).__name__}, Баланс: {self._balance} SOM"

    def get_bank_name(self) -> str:
        return self.bank_name

    def bonus_for_level(self) -> float:
        return self.hero.lvl * 10

    def __str__(self) -> str:
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            if type(self.hero) is type(other.hero):
                return self._balance + other._balance
            else:
                return "Ошибка: Нельзя сложить счета героев разных классов!"
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, BankAccount):
            same_class = type(self.hero) is type(other.hero)
            same_lvl = self.hero.lvl == other.hero.lvl
            return same_class and same_lvl
        return False


if __name__ == "__main__":
    mage1 = MageHero(name="Merlin", lvl=50, hp=100, mp=150)
    mage2 = MageHero(name="Merlin", lvl=50, hp=120, mp=200)
    warrior = WarriorHero(name="Conan", lvl=50, hp=300)

    print(mage1.action())
    print(warrior.action())

    acc1 = BankAccount(hero=mage1, balance=5000, password="secret_mage_1")
    acc2 = BankAccount(hero=mage2, balance=3000, password="secret_mage_2")
    acc3 = BankAccount(hero=warrior, balance=4000, password="secret_warrior")

    print(acc1)
    print(acc2)
    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    print("\n=== Проверка __add__ ===")
    print("Сумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)

    print("\n=== Проверка __eq__ ===")
    print("Mage1 == Mage2 ?", acc1 == acc2)
    print("Mage1 == Warrior ?", acc1 == acc3)
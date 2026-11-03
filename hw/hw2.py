import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}!")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает. Здоровье: {self.health}")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} атакует из-под тишка!")


warrior = Warrior("Воин", 5, 100, 20, 80)
mage = Mage("Маг", 5, 80, 30, 100)
assassin = Assassin("Ассасин", 5, 90, 25, 95)

warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assassin.greet()
assassin.attack()
assassin.rest()

# Мини-игра "Камень, ножницы, бумага"

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

opponents = [warrior, mage, assassin]

print("\n=== ИГРА КАМЕНЬ, НОЖНИЦЫ, БУМАГА ===")

print("Выберите героя:")
print("Warrior")
print("Mage")
print("Assassin")

choice = input("Ваш выбор: ").lower()

if choice not in heroes:
    print("Такого героя нет!")
else:
    player = heroes[choice]
    enemy = random.choice(opponents)

    print(f"\nВы выбрали: {player.name}")
    print(f"Противник: {enemy.name}")

    if player == enemy:
        print("Ничья!")

    elif (
            (player == warrior and enemy == assassin) or
            (player == assassin and enemy == mage) or
            (player == mage and enemy == warrior)
    ):
        print(f"{player.name} победил!")

    else:
        print(f"{enemy.name} победил!")

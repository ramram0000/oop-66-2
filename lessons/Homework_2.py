import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье до {self.health}")

class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")

warrior = Warrior("Воин", 1, 100, 20, 50)
mage = Mage("Маг", 1, 80, 25, 100)
assassin = Assassin("Ассасин", 1, 90, 30, 80)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

choice = input("Выберите героя: Warrior / Mage / Assassin\n").lower()

if choice not in heroes:
    print("Неверный выбор!")
else:
    player = heroes[choice]
    enemy = random.choice(list(heroes.values()))

    print(f"\nВы выбрали: {player.name}")
    print(f"Противник: {enemy.name}\n")

    if player == enemy:
        print("Ничья!")
    elif (
        (isinstance(player, Warrior) and isinstance(enemy, Assassin)) or
        (isinstance(player, Assassin) and isinstance(enemy, Mage)) or
        (isinstance(player, Mage) and isinstance(enemy, Warrior))
    ):
        print(f"{player.name} победил!")
    else:
        print(f"{enemy.name} победил!")
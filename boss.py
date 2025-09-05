import random
from enemy import Enemy

class fireDragon(Enemy):
    """
    This is our dragon blueprint 
    """
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.name = name
        self.health = 300
        self.attack_power = 40
        self.ability = "burn"
        print(f"Boss {self.name} colored {self.color} has been created with {self.health} health and {self.attack_power} attack power as well as a {self.ability} attack!")

    def attack(self):
        if self.health < 200:
            self.attack_power = 60
        elif self.health < 150:
            self.attack_power = 80
        elif self.health < 100:
            self.attack_power = 100
        elif self.health < 50:
            self.attack_power = 120
        return self.attack_power
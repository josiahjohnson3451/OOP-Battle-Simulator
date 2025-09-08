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
        self.burn_once = False
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
    

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    def is_alive(self):
        return self.health > 0
    
    def burn(self, hero):
        if self. health < 175 and not self.burn_once and hero.burn == 0:
            print(f"{self.name} uses its burn ability! {hero.name} is now burned and will take additional damage over time!")
            hero.burn = 1
            self.burn_once = True
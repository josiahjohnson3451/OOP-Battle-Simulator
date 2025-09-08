from enemy import Enemy

class BabyElf(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.name = name
        print(f"Baby Elf {self.name} has been created with {self.health} health and a {self.color} color!")
    
    def take_damage(self, damage):
       self.health -= damage
       print("Cry! How could you hit a baby 😭, YOU MONSTER!")
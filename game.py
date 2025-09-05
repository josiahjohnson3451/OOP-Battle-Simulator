import random
from goblin import Goblin
from hero import Hero
from boss import fireDragon

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Gandalf")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of stats
    defeated_goblins = 0
    total_damage = 0
    rounds = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        total_damage += damage
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                total_damage += damage
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    print(f"Rounds fought: {rounds}")
    print(f"Total damage dealt by hero: {total_damage}")
    print(f"Hero's remaining health: {hero.health}")
    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")


    if hero.is_alive():
        print("Boss fight time")
        fireDragon = fireDragon("Smaug", "red")
        while hero.is_alive() and fireDragon.is_alive():
            print("\nNew Boss Round!")
            rounds += 1
            
            # Hero's turn to attack the boss
            damage = hero.strike()
            total_damage += damage
            print(f"Hero attacks {fireDragon.name} for {damage} damage!")
            fireDragon.take_damage(damage)

            # Check if the boss was defeated
            if not fireDragon.is_alive():
                print(f"{fireDragon.name} has been defeated!")

            # Boss's turn to attack
            if fireDragon.is_alive():
                damage = fireDragon.attack()
                total_damage += damage
                print(f"{fireDragon.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
if __name__ == "__main__":
    main()

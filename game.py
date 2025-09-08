import random
from goblin import Goblin
from hero import Hero
from boss import fireDragon
from baby_elf import BabyElf

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
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
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

# Baby Elf battle section, where the hero faces off against baby elves after defeating the goblins.
    






#-----------------------------------------------------------------
# Boss battle section, where the hero faces off against the fire dragon boss after defeating the goblins.
#-----------------------------------------------------------------

    # Boss fight if hero is still alive after goblin battles
    defeated_bosses = 0





#-----------------------------------------------------------------
# Boss battle section, where the hero faces off against the fire dragon boss after defeating the goblins.
#-----------------------------------------------------------------

    # Boss fight if hero is still alive after goblin battles
    defeated_bosses = 0

    if hero.is_alive():
        print("BOSS BATTLE")
    
    while hero.is_alive and any(dragon.is_alive() for dragon in fireDragon):
        print("\nNew Boss Round!")
        rounds += 1
        
    #Hero's turn to attack the boss
    damage = hero.strike()
    if damage > 0:
        target_fireDragon = random.choice([dragon for dragon in fireDragon if dragon.is_alive()])
        print(f"Hero attacks {target_fireDragon.name} for {damage} damage!")
        target_fireDragon.take_damage(damage)

        if not target_fireDragon.is_alive():
            defeated_bosses += 1
            print(f"{target_fireDragon.name} has been defeated!")
    
    #Dragons' turn to attack
    for dragon in fireDragon:
        if dragon.is_alive():
            if dragon.health < 175 and not dragon.burn_once and hero.burn == 0:
                dragon.burn(hero)
            elif hero.is_alive() and dragon.is_alive():
                damage = dragon.attack()
                print(f"{dragon.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                total_damage += damage

    
# Final tally of bosses defeated

    if hero.is_alive():
        print(f"\nThe hero has defeated all the bosses! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated by the bosses. Game Over. (｡•́︿•̀｡)")

    #STATS
    print(f"\nTotal damage dealt: {total_damage}")
    print(f"\nTotal rounds fought: {rounds}")
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print(f"\nTotal baby elves defeated: {defeated_babyElfs} / {len(babyElfs)}")
    print(f"\nTotal bosses defeated: {defeated_bosses} / {len(fireDragon)}")



    # Determine outcome
    #if hero.is_alive():
    #    print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    #else:
    #    print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
    #print(f"Rounds fought: {rounds}")
    #print(f"Total damage dealt by hero: {total_damage}")
    #print(f"Hero's remaining health: {hero.health}")
    # Final tally of goblins defeated
    #print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()

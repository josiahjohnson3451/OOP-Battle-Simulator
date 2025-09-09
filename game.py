import random
from goblin import Goblin
from hero import Hero
from boss import fireDragon  
from baby_elf import BabyElfs

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    hero = Hero("Aragorn")
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]
    defeated_goblins = 0
    total_damage = 0
    rounds = 0

    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        total_damage += damage

        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                total_damage += damage

    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

    babyElfs = [BabyElfs(f"Baby Elf {i+1}", "Green") for i in range(2)]
    defeated_babyElfs = 0

    if hero.is_alive():
        print("\nNow the hero will face off against the baby elves!")
        while hero.is_alive() and any(babyElf.is_alive() for babyElf in babyElfs):
            print("\nNew Baby Elf Round!")
            rounds += 1
            target_babyElf = random.choice([babyElf for babyElf in babyElfs if babyElf.is_alive()])
            damage = hero.strike()
            if damage > 0:
                print(f"Hero attacks {target_babyElf.name} for {damage} damage!")
                target_babyElf.take_damage(damage)
                total_damage += damage

                if not target_babyElf.is_alive():
                    defeated_babyElfs += 1
                    print(f"{target_babyElf.name} has been defeated!")
            
            for babyElf in babyElfs:
                if babyElf.is_alive():
                    damage = babyElf.attack()
                    print(f"{babyElf.name} attacks hero for {damage} damage!")
                    hero.receive_damage(damage)
                    total_damage += damage

    fireDragons = [fireDragon(f"Fire Dragon {i+1}", "Red") for i in range(1)]
    defeated_bosses = 0

    if hero.is_alive():
        print("BOSS BATTLE")
        while hero.is_alive() and any(dragon.is_alive() for dragon in fireDragons):
            print("\nNew Boss Round!")
            rounds += 1
            target_fireDragon = random.choice([dragon for dragon in fireDragons if dragon.is_alive()])
            damage = hero.strike()
            if damage > 0:
                print(f"Hero attacks {target_fireDragon.name} for {damage} damage!")
                target_fireDragon.take_damage(damage)
                total_damage += damage

                if not target_fireDragon.is_alive():
                    defeated_bosses += 1
                    print(f"{target_fireDragon.name} has been defeated!")
            
            for dragon in fireDragons:
                if dragon.is_alive():
                    hero_burn = getattr(hero, "burn", 0)
                    if dragon.health < 175 and not getattr(dragon, "burn_once", False) and hero_burn == 0:
                        dragon.burn(hero)
                    elif hero.is_alive() and dragon.is_alive():
                        damage = dragon.attack()
                        print(f"{dragon.name} attacks hero for {damage} damage!")
                        hero.receive_damage(damage)
                        total_damage += damage

        if hero.is_alive():
            print(f"\nThe hero has defeated all the bosses! ༼ ᕤ◕◡◕ ༽ᕤ")
        else:
            print(f"\nThe hero has been defeated by the bosses. Game Over. (｡•́︿•̀｡)")

    print(f"\nTotal damage dealt: {total_damage}")    
    print(f"\nTotal rounds fought: {rounds}")
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print(f"\nTotal baby elves defeated: {defeated_babyElfs} / {len(babyElfs)}")
    print(f"\nTotal bosses defeated: {defeated_bosses} / {len(fireDragons)}")

if __name__ == "__main__":
    main()
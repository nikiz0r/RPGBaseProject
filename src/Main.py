from src import Events
from src.Characters import Hero
from random import choice
from src.Monsters import Monsters
from src.Items import Items
from src.Helpers import Helpers


def main():
    # instances
    m = Monsters()
    i = Items().ItemList
    h = Helpers()

    monsterList = m.MonsterList

    # Hero init
    hero = Hero(0, "Charlinho", 1, 0, 20, 5, 1, 1)
    hero.Equipment['hand'].append(h.getById(i, 0))

    # update armor and damage
    hero.setTotalArmor()
    hero.setTotalDamage()

    # Prologue
    Events.showMessage("You are playing with %s, a brave hero who only desires to be a student!", hero.Name)

    # mob encounter
    mob = choice(monsterList)

    if mob is not None:
        Events.showMessage("A wild %s has appeared!", mob.Name)

    # Start battle
    # Game over condition: Hero's life drop to 0
    while hero.CurrentHP > 0 and mob.CurrentHP > 0:
        key = input("\nAttack: 1\nDefend: 2\n")

        if key == "1":
            hero.attack(mob)
        elif key == "2":
            hero.defend()

        if mob.CurrentHP > 0:
            mob.attack(hero)

        Events.showStats(hero)
        Events.showStats(mob)

    if mob.CurrentHP <= 0:
        Events.showMessage("%s has slain 1 %s.\n", (hero.Name, mob.Name))
        itemDropped = Events.lootDrop(mob)
        if itemDropped is not None:
            Events.showMessage("%s has dropped!\nEquip the item? (Y or N)", itemDropped['DESCRIPTION'])
            getItem = str(input())
            if getItem.upper() == "Y":
                hero.Equipment[itemDropped['SLOT']].pop(0)
                hero.Equipment[itemDropped['SLOT']].append(itemDropped)

            # IT WORKS!
            print(hero.Equipment)
    elif hero.CurrentHP <= 0:
        Events.showMessage("%s has been split in two by %s.\nGAME OVER!", (hero.Name, mob.Name))

# Start
main()
input()

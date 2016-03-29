from BaseCharacter import StanceMachine
from Characters import Hero, MonsterList
from Items import Items
import Events

def main():
    ItemsList = Items()
    MonstersList = MonsterList()

    # Hero init
    hero = Hero("Charlinho", 1, 0, 100, 20, 1, 1)

    # testes
    '''
    hero.Equipment['head'].append(ItemsList.IronHelmet)
    hero.Equipment['chest'].append(ItemsList.IronArmor)
    hero.Equipment['feet'].append(ItemsList.IronGreaves)
    hero.Equipment['offHand'].append(ItemsList.Buckler)
    hero.Equipment['hand'].append(ItemsList.BronzeSword)
    '''
    hero.Equipment['hand'].append(ItemsList.SilverSword)

    # update armor and damage
    hero.setTotalArmor()
    hero.setTotalDamage()

    #fight simulation
    mob = MonstersList.Skeleton

    #Start battle
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

#Start
main()
input()
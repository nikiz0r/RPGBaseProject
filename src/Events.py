from random import random
from bisect import bisect
import time


def showMessage(message, variables, delay=1):
    time.sleep(delay)
    print(message % variables)


def showStats(target):
    showMessage("%s\nHP: %s/%s\nMP: %s/%s\nDamage: %s\nArmor: %s\n", (target.Name, target.CurrentHP if target.CurrentHP > 0 else 0,
                                                                      target.MaxHP, target.CurrentMP, target.MaxMP,
                                                                      target.Damage, target.Armor), 2)


def stanceChange(target, stance):
    print("%s changed its stance to %s" % (target.Name, stance))
    target.Stance = stance


def lootDrop(monster):
    itemDropped = None

    if random() < monster.DropRate:
        dropItems = []
        for item in monster.DropItems:
            dropItems.append((item['ID'], item['PERCENT']))
        itemDropped = weighedChoice(dropItems)
    return itemDropped


def weighedChoice(choices): # esse kra eu peguei na net, nao parei pra entender direito como que funciona
    values, weights = zip(*choices)
    total = 0
    cumWeights = []
    for w in weights:
        total += w
        cumWeights.append(total)
    x = random() * total
    i = bisect(cumWeights, x)
    return values[i]

def levelUp(target): # TODO: desenvolver essa parte
    pass
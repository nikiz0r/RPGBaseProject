import random
import Events
from BaseCharacter import BaseCharacter, StanceMachine


class MonsterList:
    def __init__(self):
        self.Skeleton = BasicMonster("Skeleton", 1, 0, 10, 0, 3, 0)
        self.Gargoyle = BasicMonster("Gargoyle", 3, 0, 30, 5, 5, 1)


class Hero(BaseCharacter):
    def __init__(self, name, level, experience, hp, mp, baseDamage, baseArmor):
        BaseCharacter.__init__(self, name, level, experience, hp, mp, baseDamage, baseArmor)
        self.Equipment = {
            'head': [],
            'hand': [],
            'chest': [],
            'feet': [],
            'offHand': []
        }

    def setTotalArmor(self):
        totalArmor = self.BaseArmor
        totalArmor += \
            self.Equipment['head'][0]['ARMOR'] if len(self.Equipment['head']) > 0 else 0 +\
            self.Equipment['chest'][0]['ARMOR'] if len(self.Equipment['chest']) > 0 else 0 +\
            self.Equipment['feet'][0]['ARMOR'] if len(self.Equipment['feet']) > 0 else 0 +\
            self.Equipment['offHand'][0]['ARMOR'] if len(self.Equipment['offHand']) > 0 else 0 +\
            self.Equipment['hand'][0]['ARMOR'] if len(self.Equipment['hand']) > 0 else 0
        self.Armor = totalArmor

    def setTotalDamage(self):
        totalDamage = self.BaseDamage
        totalDamage += \
            self.Equipment['head'][0]['DAMAGE'] if len(self.Equipment['head']) > 0 else 0 +\
            self.Equipment['chest'][0]['DAMAGE'] if len(self.Equipment['chest']) > 0 else 0 +\
            self.Equipment['feet'][0]['DAMAGE'] if len(self.Equipment['feet']) > 0 else 0 +\
            self.Equipment['offHand'][0]['DAMAGE'] if len(self.Equipment['offHand']) > 0 else 0 +\
            self.Equipment['hand'][0]['DAMAGE'] if len(self.Equipment['hand']) > 0 else 0
        self.Damage = totalDamage

    def attack(self, target):
        if self.Stance == StanceMachine.Defend:
            Events.stanceChange(self, StanceMachine.Attack)

        damageMultiplier = 2 if random.randint(self.Equipment['hand'][0]['CRITP'], 10) <= \
                                self.Equipment['hand'][0]['CRITP'] else 1 # 2 = crit
        damage = self.Damage * damageMultiplier
        target.CurrentHP -= damage if damage > target.Armor else 0

        print("%s attacks." % self.Name)
        if damageMultiplier == 2:
            print("It's a critical hit!")
        print("It deals %s damage to %s." % (damage, target.Name))

    def defend(self):
        Events.stanceChange(self, StanceMachine.Defend)


class BasicMonster(BaseCharacter):
    def __init__(self, name, level, experience, hp, mp, baseDamage, baseArmor):
        BaseCharacter.__init__(self, name, level, experience, hp, mp, baseDamage, baseArmor)

    def attack(self, target):
        # verify if target is defending
        armor = (3 if target.Stance == StanceMachine.Defend else 1) * target.Armor

        # rageMode procs at 30% hp
        if self.CurrentHP <= self.MaxHP * 0.3:
            print("%s is enraged. (Causes double damage)" % self.Name)
            damage = 0 if armor >= self.Damage * 2 else self.Damage * 2 - armor
        else:
            damage = 0 if armor >= self.Damage else self.Damage - armor

        target.CurrentHP -= damage
        print("%s attacks." % self.Name)
        print("It deals %s damage to %s." % (damage, target.Name))

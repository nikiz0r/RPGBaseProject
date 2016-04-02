from random import random
from src import Events
from src.BaseCharacter import BaseCharacter, StanceMachine


class Hero(BaseCharacter):
    def __init__(self, id, name, level, experience, hp, mp, baseDamage, baseArmor):
        BaseCharacter.__init__(self, id, name, level, experience, hp, mp, baseDamage, baseArmor)
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

        damageMultiplier = 2 if (random() * 100) <= self.Equipment['hand'][0]['CRITP'] else 1 # 2 = crit
        damage = self.Damage * damageMultiplier if self.Damage * damageMultiplier> target.Armor else 0
        target.CurrentHP -= damage

        Events.showMessage("%s attacks.", self.Name)
        if damageMultiplier == 2:
            Events.showMessage("It's a critical hit!%s", "")
        Events.showMessage("It deals %s damage to %s.", (damage, target.Name))

    def defend(self):
        Events.stanceChange(self, StanceMachine.Defend)

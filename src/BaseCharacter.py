from src import Events


class BaseCharacter:
    def __init__(self, id, name, level, experience, hp, mp, baseDamage, baseArmor):
        self.Id = id
        self.Name = name
        self.Level = level
        self.Experience = experience
        self.MaxHP = hp
        self.CurrentHP = hp
        self.CurrentMP = mp
        self.MaxMP = mp
        self.BaseDamage = baseDamage
        self.Damage = baseDamage
        self.BaseArmor = baseArmor
        self.Armor = baseArmor
        self.Stance = StanceMachine.Attack


class BaseMonster(BaseCharacter):
    def __init__(self, id, name, level, experience, hp, mp, baseDamage, baseArmor, dropItems, dropRate):
        BaseCharacter.__init__(self, id, name, level, experience, hp, mp, baseDamage, baseArmor)
        self.DropItems = dropItems
        self.DropRate = dropRate

    def attack(self, target):
        # verify if target is defending
        armor = (3 if target.Stance == StanceMachine.Defend else 1) * target.Armor

        # rageMode procs at 30% hp
        if self.CurrentHP <= self.MaxHP * 0.3:
            Events.showMessage("%s is enraged. (Causes double damage)", self.Name)
            damage = 0 if armor >= self.Damage * 2 else self.Damage * 2 - armor
        else:
            damage = 0 if armor >= self.Damage else self.Damage - armor

        target.CurrentHP -= damage
        Events.showMessage("%s attacks.", self.Name)
        Events.showMessage("It deals %s damage to %s.\n", (damage, target.Name))


class StanceMachine:
    Attack = "Attacking"
    Defend = "Defending"

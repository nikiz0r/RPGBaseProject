class BaseCharacter:
    def __init__(self, name, level, experience, hp, mp, baseDamage, baseArmor):
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


class StanceMachine:
    Attack = "Attacking"
    Defend = "Defending"

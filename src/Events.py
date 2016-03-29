

def showStats(target):
    print("\n%s\nHP: %s/%s\nMP: %s/%s\nDamage: %s\nArmor: %s" % (target.Name, target.CurrentHP, target.MaxHP,
                                                                 target.CurrentMP, target.MaxMP, target.Damage,
                                                                 target.Armor))


def stanceChange(target, stance):
    print("%s changed its stance to %s" % (target.Name, stance))
    target.Stance = stance

from src.BaseCharacter import BaseMonster
from src.Items import Items
from src.Helpers import Helpers


class Monsters:
    def __init__(self):
        h = Helpers()
        i = Items()

        self.MonsterList = []

        self.MonsterList.append(
            BaseMonster(1, "Skeleton", 1, 10, 5, 0, 3, 0,
                        [{'ID': h.getByDescription(i.ItemList, "Bronze Sword"), 'PERCENT': 0.1},
                         {'ID': h.getByDescription(i.ItemList, "Iron Helmet"), 'PERCENT': 0.1}], 0.3)
        )
        self.MonsterList.append(
            BaseMonster(2, "Gargoyle", 2, 20, 10, 0, 5, 1, [{'ID': h.getByDescription(i.ItemList, "Buckler"), 'PERCENT': 0.2}],
                        0.2)
        )
        self.MonsterList.append(
            BaseMonster(99, "Math Test", 10, 100, 200, 30, 20, 15,
                        [{'ID': h.getById(i.ItemList, 99), 'PERCENT': 0.5}],
                        0.5)
        )



class Items:
    def __init__(self):
        self.ItemList = []

        self.ItemList.append(
            {
                'ID': 0,
                'DESCRIPTION': "Empty Hands",
                'DAMAGE': 1,
                'ARMOR': 0,
                'SLOT': "hand",
                'CRITP': 0  # Crit percentage
            }
        )

        self.ItemList.append(
            {
                'ID': 1,
                'DESCRIPTION': "Bronze Sword",
                'DAMAGE': 4,
                'ARMOR': 0,
                'SLOT': "hand",
                'CRITP': 1 # Crit percentage
            }
        )
        self.ItemList.append(
            {
                'ID': 2,
                'DESCRIPTION': "Silver Sword",
                'DAMAGE': 10,
                'ARMOR': 0,
                'SLOT': "hand",
                'CRITP': 2  # Crit percentage
            }
        )
        self.ItemList.append(
            {
                'ID': 3,
                'DESCRIPTION': "Iron Helmet",
                'DAMAGE': 0,
                'ARMOR': 1,
                'SLOT': "head"
            }
        )
        self.ItemList.append(
            {
                'ID': 4,
                'DESCRIPTION': "Iron Armor",
                'DAMAGE': 0,
                'ARMOR': 2,
                'SLOT': "chest"
            }
        )
        self.ItemList.append(
            {
                'ID': 5,
                'DESCRIPTION': "Iron Greaves",
                'DAMAGE': 0,
                'ARMOR': 1,
                'SLOT': "feet"
            }
        )
        self.ItemList.append(
            {
                'ID': 6,
                'DESCRIPTION': "Buckler",
                'DAMAGE': 0,
                'ARMOR': 3,
                'SLOT': "offHand"
            }
        )
        self.ItemList.append(
            {
                'ID': 99,
                'DESCRIPTION': "Math Book",
                'DAMAGE': 40,
                'ARMOR': 0,
                'SLOT': "hand",
                'CRITP': 4  # Crit percentage
            }
        )

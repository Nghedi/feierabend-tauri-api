
Back = 3
Boots = 11
Chest = 4
Gloves = 8
Head = 0
Legs = 10
Mainhand = 16
Neck = 1
Offhand = 17
Ranged = 18
Ring = 12
Ringtwo = 13
Shoulder = 2
Shirt = 6
Tabard = 5
Trinket = 14
Trinkettwo = 15
Wrist = 7
Waist = 9

DK = 6
Druid = 11
Hunter = 3
Mage = 8
Paladin = 2
Priest = 5
Rogue = 4
Shaman = 7
Warlock = 9
Warrior = 1

def isClass(playerdata, WOWclass):
    return (playerdata['class'] == WOWclass)

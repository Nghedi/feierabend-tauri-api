import json
from color import color

from enchants import *
from gems import *
from professions import *
from roster import *

from tauri_stuff import *

valid_professions = ok_professions

def loadPlayerFile(name):
    with open('data/'+ name + '.json') as f:
      players[name]['data'] = json.load(f)

def checkProfessions(playerdata, role):
    return_value = True
    if 'primary_trade_skill_1' not in playerdata:
        print(color.RED+"WHOOT Empty Profession"+color.END)
        return_value = False
    else:
        return_value = return_value and professionIsValid(playerdata['primary_trade_skill_1']['name'],role) 
        return_value = return_value and professionIsValid(playerdata['primary_trade_skill_2']['name'],role) 

    if 'primary_trade_skill_2' not in playerdata:
        print(color.RED+"WHOOT Empty Profession"+color.END)
        return_value = False
    else:
        return_value = return_value and professionIsHighEnough(playerdata['primary_trade_skill_1']['name'],playerdata['primary_trade_skill_1']['value'])
        return_value = return_value and professionIsHighEnough(playerdata['primary_trade_skill_2']['name'],playerdata['primary_trade_skill_2']['value'])

    if (return_value == True):
        print("Professions alright")

def isProfession(playerdata, profession):
    if 'primary_trade_skill_1' in playerdata:
        if (playerdata['primary_trade_skill_1']['name'] == profession):
            return True
    if ('primary_trade_skill_2' in playerdata):
        if (playerdata['primary_trade_skill_2']['name'] == profession):
            return True
    return False

def professionIsValid(profession, role):
    if profession not in valid_professions[role]:
        print(color.RED,profession, "is not a valid profession for", role, color.END)
        return False
    return True

def professionIsHighEnough(profession, skill):
    if skill < professions_required_level[profession]:
        print(color.YELLOW+"Professions ", profession, " has skill ", skill, " (", professions_required_level[profession], " required)."+color.END, sep='') 
        return False
    return True

def checkGems():
    return

def checkEnchants(playerdata, role):
    checkEnchantsBack(playerdata, role)
    checkEnchantsBoots(playerdata, role)
    checkEnchantsChest(playerdata, role)
    checkEnchantsGloves(playerdata, role)
    checkEnchantsHead(playerdata, role)
    checkEnchantsLeg(playerdata, role)
    checkEnchantsMainhand(playerdata, role)
    checkEnchantsOffhand(playerdata, role)
    checkEnchantsRanged(playerdata, role)
    checkEnchantsShoulder(playerdata, role)
    checkEnchantsRing(playerdata, role)
    checkEnchantsWrist(playerdata, role)
    checkEnchantsWaist(playerdata, role)

def checkEnchantsBack(playerdata, role):
    if (isProfession(playerdata, "Tailoring")
        or isProfession(playerdata, "Engineering")):
        return True
    slot = Back 
    return True

def checkEnchantsBoots(playerdata, role):
    if (isProfession(playerdata, "Engineering")):
        return True
    slot = Boots
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsChest(playerdata, role):
    slot = Chest
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsGloves(playerdata, role):
    if (isProfession(playerdata, "Engineering")):
        return True
    slot = Gloves
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsHead(playerdata, role):
    slot = Head
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsLeg(playerdata, role):
    if (isProfession(playerdata, "Leatherworking")
        or isProfession(playerdata, "Tailoring")):
        return True
    slot = Legs
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsMainhand(playerdata, role):
    if isClass(playerdata, DK):
        return True

    slot = Mainhand
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsOffhand(playerdata, role):
    if isClass(playerdata, DK):
        return True

    if not (isClass(playerdata, Warrior)
            or isClass(playerdata, Paladin)
            or isClass(playerdata, Shaman)):
        return True

    slot = Offhand
    if playerdata['characterItems'][17]['entry'] == 0:
        return True
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsRanged(playerdata, role):
    if not (isClass(playerdata, Warrior)
            or isClass(playerdata, Rogue)
            or isClass(playerdata, Hunter)):
        return True
    slot = Ranged
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsRing(playerdata, role):
    return True 
    slot = Ring
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsShoulder(playerdata, role):
    if (isProfession(playerdata, "Inscription")):
        print('bla')
        return True

    slot = Shoulder 
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False

    if not (playerdata['characterItems'][slot]['ench']['enchantid'] in bis_enchants[role][Shoulder]):
        print(color.RED+playerdata['characterItems'][slot]['name'], "has no valid enchant."+color.END)
        return False
    print('bla')
    return True

def checkEnchantsWrist(playerdata, role):
    if (isProfession(playerdata, "Leatherworking")):
        return True
    slot = Wrist
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False
    return True 

def checkEnchantsWaist(playerdata, role):
    return True 
    slot = Waist
    if not checkEnchantsIsEnchanted(playerdata, slot):
        return False

def checkEnchantsIsEnchanted(playerdata, slot):
    if not playerdata['characterItems'][slot]['ench']:
        print(color.RED+playerdata['characterItems'][slot]['name'], "is missing ANY enchant."+color.END)
        return False
    return True


def checkPlayer(name):
    checkProfessions(players[name]['data'], players[name]['role'])
    checkEnchants(players[name]['data'], players[name]['role'])



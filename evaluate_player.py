import json

from enchants import *
from gems import *
from professions import *
from roster import *

valid_professions = ok_professions

def loadPlayerFile(name):
    with open('data/'+ name + '.json') as f:
      players[name]['data'] = json.load(f)

def checkProfessions(playerdata, role):
    return_value = True
    return_value = return_value and professionIsValid(playerdata['primary_trade_skill_1']['name'],role) 
    return_value = return_value and professionIsValid(playerdata['primary_trade_skill_2']['name'],role) 

    return_value = return_value and professionIsHighEnough(playerdata['primary_trade_skill_1']['name'],playerdata['primary_trade_skill_1']['value'])
    return_value = return_value and professionIsHighEnough(playerdata['primary_trade_skill_2']['name'],playerdata['primary_trade_skill_2']['value'])
    if (return_value == True):
        print("Professions alright")

def professionIsValid(profession, role):
    if profession not in valid_professions[role]:
        print(profession, "is not a valid profession for", role)
        return False
    return True

def professionIsHighEnough(profession, skill):
    if skill < professions_required_level[profession]:
        print("Professions ", profession, " has skill ", skill, " (", professions_required_level[profession], " required).", sep='') 
        return False
    return True

def checkGems():
    return

def checkEnchants(playerdata, role):
    enchantable_slots = (0, 2, 3, 4, 7, 8, 10, 11, 16, 17,)

    if (playerdata['primary_trade_skill_1']['name'] == "Enchanting)"
       or playerdata['primary_trade_skill_2']['name'] == "Enchanting)"):
        enchantable_slots = enchantable_slots.append(12)
        enchantable_slots = enchantable_slots.append(13)

    for slot in enchantable_slots: 
        if not playerdata['characterItems'][slot]['ench']:
            print(playerdata['characterItems'][slot]['name'], "is missing ANY enchant.")

def checkPlayer(name):
    role = 'shaman_resto'
    checkProfessions(players[name]['data'], role)
    checkEnchants(players[name]['data'], role)



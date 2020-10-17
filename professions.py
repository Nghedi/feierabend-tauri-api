
professions_required_level = {
    'Alchemy': 420,
    'Blacksmithing': 400, 
    'Enchanting': 400, 
    'Engineering': 405,
    'Inscription': 400, 
    'Jewelcrafting': 370,
    'Leatherworking': 400, 
    'Tailoring': 420, 
    'Mining': 450,
}

all_ok_professions = ('Jewelcrafting', 'Engineering', 'Blacksmithing', 'Tailoring', 'Leatherworking', 'Inscription', 'Enchanting', 'Alchemy')
all_ok_professions_tank = all_ok_professions + ('Mining',)

ok_professions = {
    'dk_tank': all_ok_professions,
    'dk_dps': all_ok_professions,
    'druid_feral_cat': all_ok_professions,
    'druid_feral_bear': all_ok_professions_tank,
    'druid_resto': all_ok_professions,
    'druid_moonkin': all_ok_professions,
    'hunter': all_ok_professions,
    'mage': all_ok_professions,
    'paladin_tank': all_ok_professions_tank,
    'paladin_retri': all_ok_professions,
    'paladin_holy': all_ok_professions,
    'priest': all_ok_professions,
    'rogue': all_ok_professions,
    'shaman_elemental': all_ok_professions,
    'shaman_enhancer': all_ok_professions,
    'shaman_resto': all_ok_professions,
    'warlock': all_ok_professions,
    'warrior_dps': all_ok_professions,
    'warrior_tank': all_ok_professions_tank,
}
bis_professions = {
    'shaman_elemental': ('Engineering', 'Jewelcrafting', 'Blacksmithing', 'Tailoring'),
    'shaman_enhancer': ('Engineering', 'Jewelcrafting', 'Blacksmithing'),
    'shaman_resto': ('Engineering', 'Jewelcrafting', 'Blacksmithing'),
}

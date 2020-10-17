#!/usr/bin/python3

from tauri_api_wrapper import *
from roster import *

for key in players_speerspitze:
    print(key)
    getPlayerData(key)

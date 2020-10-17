#!/usr/bin/python3

import json
import urllib.request
import urllib.parse
import ssl
import os

API_KEY=os.environ['TAURI_API_KEY']
API_SECRET=os.environ['TAURI_API_SECRET']
REALM = 'Crystalsong'

url = 'https://chapi.tauri.hu/apiIndex.php?apikey='+API_KEY

def getGuildList(name):
    data = json.dumps({'secret': API_SECRET, 'url' : 'guild-info', 'params' : {'r': REALM, 'gn': name}}).encode("utf-8")
    f = urllib.request.urlopen(url, data=data, context=ssl._create_unverified_context())
    ou = f.read().decode('utf-8')
    outputdata = json.loads(ou)
    return outputdata

def getPlayerData(name):
    data = json.dumps({'secret': API_SECRET, 'url' : 'character-sheet', 'params' : {'r': REALM, 'n': name}}).encode("utf-8")
    f = urllib.request.urlopen(url, data=data, context=ssl._create_unverified_context())
    ou = f.read().decode('utf-8')
    data = json.loads(ou)
    outputdata = data['response']
    with open('data/'+name+'.json', 'w') as outfile:
        json.dump(outputdata, outfile, indent=4, sort_keys=True)

def getPlayerReputation(name):
    data = json.dumps({'secret': API_SECRET, 'url' : 'character-reputation', 'params' : {'r': REALM, 'n': name}}).encode("utf-8")
    f = urllib.request.urlopen(url, data=data, context=ssl._create_unverified_context())
    ou = f.read().decode('utf-8')
    outputdata = json.loads(ou)
    return outputdata

getPlayerData('Nghedk')

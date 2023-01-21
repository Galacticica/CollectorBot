import discord
import random
import datetime
from datetime import date
import json
from discord.ext import commands, tasks
from random import randint


async def update_cards(ctx, serverID, file="cards.json"):
    with open(file) as cd:
        main_database = json.load(cd)
        main_cards = main_database.keys()
    cd.close()
    serverFile = str(serverID) + '_' + file
    with open(serverFile) as sd:
        server_database = json.load(sd)
        server_cards = server_database.keys()
    sd.close()
    common_cards = [card for card in main_cards if card in server_cards]
    missing_cards = []
    for key in main_cards:
        if key not in common_cards:
            missing_cards.append(key)
    for key in missing_cards:
        card = main_database.get(key)
        identity = card[0]
        rarity = card[1]
        franchise = card[2]
        species = card[3]
        primary = card[4]
        secondary = card[5]
        image = card[6]
        ownership = card[7]
        value = card[8]
        level = card[9]
        server_database[key] = [identity, rarity, franchise, species, primary, secondary, image, ownership, value, level]
    with open(serverFile, 'w') as sd:
        json.dump(server_database, sd, indent=2)
    sd.close()
    await ctx.send("New cards have been added to this server.")

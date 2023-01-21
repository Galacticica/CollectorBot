import discord
import random
import datetime
from datetime import date
import json
from discord.ext import commands, tasks
from random import randint



async def get_card_info(ctx, name, file="cards.json"):
    with open (file) as database:
        data = json.load(database)
        cards = data.keys()
        for x in cards:
            if name.lower() == x.lower():
                card = data.get(x)
                name = x
        name = name.replace("_", " ")
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
    card_embed = discord.Embed(title=f"{name}", description=f"Rarity: {rarity}\n"
                f"Owner: {ownership}\n"
                f"Level: {level}\n"
                f"Value: {value}\n"
                f"Franchise: {franchise}\n"
                f"Secret Identity: {identity}\n"
                f"Species: {species}\n"
                f"Primary Attack: {primary}\n"
                f"Secondary Attack: {secondary}", color=0x6622f0)
    card_embed.set_image(url=f"{image}")
    await ctx.send(embed=card_embed)
    database.close()

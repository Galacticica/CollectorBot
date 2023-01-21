import discord
import random
import datetime
from datetime import date
import json
from discord.ext import commands, tasks
from random import randint
import create_card as cc
import card_info as ci

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = 'card', intents=intents)

@client.event
async def on_ready():
    print("I Have Come.")

@client.event
async def on_guild_join(guild):
    serverID = guild.id
    file = f"{serverID}_cards.json"
    with open("cards.json") as f:
        data = json.load(f)
    f.close()
    with open(file, 'w') as new_database:
        json.dump(data, new_database, indent=2)
    new_database.close()



@client.command()
async def testing(ctx):
    await ctx.send('test')

@client.command()
async def create(ctx):
    await cc.newCardEmbed(ctx, client)

@client.command()
async def info(ctx, name):
    await ci.get_card_info(ctx, name)




token = ''
client.run(token)
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
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("I Have Come.")


@client.command()
async def testing(ctx):
    await ctx.send('test')

@client.command()
async def createCard(ctx):
    await cc.newCardEmbed(ctx, client)

@client.command()
async def cardinfo(ctx, name):
    await ci.get_card_info(ctx, name)




token = ''
client.run(token)
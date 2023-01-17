import discord
import random
import datetime
from datetime import date
import json
from discord.ext import commands, tasks
from random import randint

async def newCardEmbed(ctx, client):
    parameters = ['name', 'rarity', 'done', 'franchise', 'type', "species", "image"]
    name = ""
    rarity = ""
    franchise = ""
    fightType = ""
    species = ""
    image = "https://imgur.com/n89Pp7P"
    newEmbed = discord.Embed(title="Card Create", description="Create a new card.", color=0x6622f0)
    newEmbed.add_field(name = f"{name}", value=f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Type: {fightType}\n"
                                               f"Species: {species}")
    newEmbed.set_image(url=f"{image}")
    msg = await ctx.send(embed=newEmbed)
    while True:
        await ctx.send("What field would you like to edit?")
        msg = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
        if msg.content.lower() not in parameters:
            await ctx.send("That is not a valid parameter")
        elif msg.content.lower() == 'name':
            await ctx.send("Enter the card's name.")
            name = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
            name = name.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Type: {fightType}\n"
                                               f"Species: {species}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "rarity":
            await ctx.send("Enter the card's rarity.")
            rarity = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
            rarity = rarity.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Type: {fightType}\n"
                                               f"Species: {species}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "franchise":
            await ctx.send("Enter the card's franchise.")
            franchise = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
            franchise = franchise.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Type: {fightType}\n"
                                               f"Species: {species}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "type":
            await ctx.send("Enter the card's type.")
            fightType = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
            fightType = fightType.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Type: {fightType}\n"
                                               f"Species: {species}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "species":
            await ctx.send("Enter the card's species.")
            species = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
            species = species.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Type: {fightType}\n"
                                               f"Species: {species}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "image":
            await ctx.send("Enter the card's imgur url.")
            try:
                image = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
                image = image.content
                if "imgur.com" not in image:
                    raise ValueError
            except:
                await ctx.send("Not a valid imgur url.")
            else:
                newEmbed.set_image(url=f"{image}")
                msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "done":
            await ctx.send("Does this look correct?")
            msg = await ctx.send(embed=newEmbed)
            answer = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
            if answer.content.lower() == "yes":
                #TODO: Add card to database here
                await ctx.send("Card added to database")
                break
            else:
                pass






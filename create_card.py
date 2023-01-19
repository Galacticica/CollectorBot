import discord
import json
import random
import datetime
from datetime import date
import json
from discord.ext import commands, tasks
from random import randint

async def newCardEmbed(ctx, client):
    parameters = ['name', 'rarity', 'done', 'franchise', 'primary', "secondary", "species", "image", "cancel"]
    rarities = ["common", "uncommon", "rare", "epic", "legendary", "mythic", "special"]
    name = ""
    identity = "N/A"
    rarity = ""
    franchise = ""
    primary = ""
    secondary = ""
    species = ""
    image = "https://imgur.com/n89Pp7P.png"
    newEmbed = discord.Embed(title="Card Create", description="Create a new card.", color=0x6622f0)
    newEmbed.add_field(name = f"{name}", value=f"Secret Identity: {identity}\n"
                                               f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Species: {species}\n"
                                               f"Primary Attack: {primary}\n"
                                               f"Secondary Attack: {secondary}")
    newEmbed.set_image(url=f"{image}")
    msg = await ctx.send(embed=newEmbed)
    while True:
        await ctx.send("What field would you like to edit?")
        msg = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
        if msg.content.lower() not in parameters:
            await ctx.send("That is not a valid parameter")
        elif msg.content.lower() == 'name':
            await ctx.send("Enter the card's name.")
            name = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
            name = name.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Secret Identity: {identity}\n"
                                               f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Species: {species}\n"
                                               f"Primary Attack: {primary}\n"
                                               f"Secondary Attack: {secondary}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "rarity":
            await ctx.send("Enter the card's rarity.")
            try:
                rarity = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
                rarity = rarity.content
                rarity = rarity.capitalize()
                if rarity.lower() not in rarities:
                    raise ValueError
            except:
                await ctx.send("Not a valid rarity.")
            else:
                newEmbed.set_field_at(index=0, name = f"{name}", value=f"Secret Identity: {identity}\n"
                                                   f"Rarity: {rarity}\n"
                                                   f"Franchise: {franchise}\n"
                                                   f"Species: {species}\n"
                                                   f"Primary Attack: {primary}\n"
                                                   f"Secondary Attack: {secondary}")
                msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "franchise":
            await ctx.send("Enter the card's franchise.")
            franchise = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
            franchise = franchise.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Secret Identity: {identity}\n"
                                               f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Species: {species}\n"
                                               f"Primary Attack: {primary}\n"
                                               f"Secondary Attack: {secondary}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "primary":
            await ctx.send("Enter the card's primary attack.")
            primary = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
            primary = primary.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Secret Identity: {identity}\n"
                                               f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Species: {species}\n"
                                               f"Primary Attack: {primary}\n"
                                               f"Secondary Attack: {secondary}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "secondary":
            await ctx.send("Enter the card's secondary attack.")
            secondary = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
            secondary = secondary.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Secret Identity: {identity}\n"
                                               f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Species: {species}\n"
                                               f"Primary Attack: {primary}\n"
                                               f"Secondary Attack: {secondary}")
        elif msg.content.lower() == "species":
            await ctx.send("Enter the card's species.")
            species = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
            species = species.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Secret Identity: {identity}\n"
                                               f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Species: {species}\n"
                                               f"Primary Attack: {primary}\n"
                                               f"Secondary Attack: {secondary}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "identity":
            await ctx.send("Enter the card's secret identity.")
            identity = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
            identity = identity.content
            newEmbed.set_field_at(index=0, name = f"{name}", value=f"Secret Identity: {identity}\n"
                                               f"Rarity: {rarity}\n"
                                               f"Franchise: {franchise}\n"
                                               f"Species: {species}\n"
                                               f"Primary Attack: {primary}\n"
                                               f"Secondary Attack: {secondary}")
            msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "image":
            await ctx.send("Enter the card's imgur url.")
            try:
                image = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
                image = image.content
                if "imgur.com" not in image:
                    raise ValueError
            except:
                await ctx.send("Not a valid imgur url.")
            else:
                if '.png' not in image:
                    image = image + '.png'
                newEmbed.set_image(url=f"{image}")
                msg = await ctx.send(embed=newEmbed)
        elif msg.content.lower() == "done":
            await ctx.send("Does this look correct?")
            msg = await ctx.send(embed=newEmbed)
            answer = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60.0)
            if answer.content.lower() == "yes":
                add_card_to_database(name, identity, rarity, franchise, species, primary, secondary, image)
                await ctx.send("Card added to database")
                break
            else:
                pass
        elif msg.content.lower() == "cancel":
            await ctx.send("Card creation canceled.")
            break


def add_card_to_database(name, identity, rarity, franchise, species, primary, secondary, image, file="cards.json", owner="Not Owned", level=1):
    with open (file) as database:
        data = json.load(database)
        value = determine_value(rarity)
        #name: [identity, rarity, franchise, species, primary, secondary, image, owner, value, level]
        data[name] = [identity, rarity, franchise, species, primary, secondary, image, owner, value, level]
        write_to_database(data)


def write_to_database(data, file="cards.json"):
    with open (file, 'w') as f:
        json.dump(data, f, indent=2)

def determine_value(rarity):
    if rarity.lower() == "common":
        value = randint(50,100)
    elif rarity.lower() == "uncommon":
        value = randint(101, 200)
    elif rarity.lower() == "rare":
        value = randint(201, 300)
    elif rarity.lower() == "epic":
        value = randint(301, 400)
    elif rarity.lower() == "legendary":
        value = randint(401, 500)
    elif rarity.lower() == "mythic":
        value = randint(501, 600)
    elif rarity.lower() == "special":
        value = 1000
    else:
        value = 0
    return value





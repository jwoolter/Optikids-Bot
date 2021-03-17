import time
import discord
import os
from discord import channel
import datetime
import random
#defines discord token for bot authorization and connection
TOKEN2 = "ODIxNTYzMDE3ODI1MDkxNTk0.YFFiLw.rl6KP39uQKwZe_l71JBqvVOTHYI"
client = discord.Client()
start_time = time.time()
died_response = [
    "HAHAHA! Sean Liu yeeted your sail and you can't race. You lost $2000.",
    "Ono! Christos Atzemian didn't like the way you tacked and killed you with guns issued by the **Greek Special Forces** ",
    "Carrie Lam appeared **Surprise motherfuckas**!! You had a stomachache and left"
]
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Bot under development'))
    print(f'{client.user.name} has connected to discord and is now online')
    print("Connection time: \n")
    print("--- %s seconds ---" % (time.time() - start_time))
@client.event
async def on_member_join(member):
    await member.create_dm()
    embedVar = discord.Embed(title="Welcome", description="What's up nerd! Don't forget to check out this superior bot! ", color=0xff0000)
    embedVar.add_field(name="Let's get started!", value="Type: (-mc help) to get started!!", inline=False)
    await member.dm_channel.send(f'Hi {member.name}')
    await member.dn_channel.send(embed=embedVar)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "/help" in message.content.lower():
        embedVar = discord.Embed(title="Guide for OptiKids on discord", description="~Never gonna give you up~", color=0x00fe00)
        embedVar.add_field(name="Start Playing", value="Type: (/create profile) to create a profile and start playing!! " , inline=True)
        embedVar.add_field(name="View inventionary", value="Type (/invent) to view your inventory", inline=False)
        embedVar.add_field(name="Shop", value="Type (/shop) to view the shop")
        await message.channel.send(embed=embedVar)
    if message.content.startswith("/create profile"):
        username = message.author.id
        usernamed = str(username) + ".txt"
        str(usernamed)
        existing_users = os.listdir()
        if str(usernamed) in existing_users:
            await message.channel.send("{} Your profile exists, don't try to break me.".format(message.author.mention)) 
        else:
            await message.channel.send("Okay {} I am now creating your user profile".format(message.author.mention))
            print(username)
            filename = str(username) +".txt"
            str(filename)
            file = open(filename, "w")
            file.write(str(username))
            file.write("\n")
            file.write("stock used opti")
            file.write("\n")
            file.write("Far East Spars")
            file.write("\n")
            file.write("Far East Sail")
            file.write("\n")
            file.write("Wooden foils")
            file.write("\n")
            file.write("0")
            file.close()
            await message.channel.send("Okay {} I have created your user profile, type **/invent** to check your inventory!".format(message.author.mention))
    if message.content.startswith("/invent"):
        await message.channel.send("{} Here is your inventory.".format(message.author.mention))
        username1 = message.author.id
        print(username1)
        usernamed1 = str(username1) + ".txt"
        usernamed1= str(usernamed1)
        name = message.author.name
        file = open(usernamed1, "r")
        lines = file.readlines()
        boat = lines[1]
        spars = lines[2]
        sail = lines[3]
        foils = lines[4]
        money = lines[5]
        embedVar = discord.Embed(title=name+"'s inventionary", color=0x123456)
        embedVar.add_field(name="Boat", value=boat, inline=True)
        embedVar.add_field(name="Spars", value=spars, inline=True)
        embedVar.add_field(name="Sail", value=sail, inline=True)
        embedVar.add_field(name="Foils", value=foils, inline=True)
        embedVar.add_field(name="Money", value=money,inline=True)
        await message.channel.send(embed=embedVar)
    if message.content.startswith("/shop"):
        embedVar= discord.Embed(title="Opti Shop!", color = 0xff00ff)
        embedVar.add_field(name="BOATS", value="1. Stock used boat \n 2. The Melting French Optimist \n 3. Far  East Optimist \n 4. Nautivela \n 5. Blue Blue Optimist \n 6. Winner Optimist", inline=False)
        embedVar.add_field(name="SPARS", value="1. Far East Spars \n 2. Black Gold Spars \n 4. Optimax Mk1 \n 5. Optimax Mk2 \n 6. Optimax Mk3", inline=False)
        embedVar.add_field(name="SAILS", value="1. Far East Sail \n 2. Olympic Sail \n 3. J sail Green \n 4. J sail Blue \n 5. J sail Red \n 6. J sail Black \n 7. OneSail \n 8. OneSail Pro", inline=False)
        embedVar.add_field(name="FOILS", value="1. Wooden foils \n 2. Plastic foils \n 3. Far East foils \n 4. DSK foils \n 5. Waszp Foils")
        await message.channel.send(embed=embedVar)
    if message.content.startswith("/cruise"):
        output = random.randint(1,100)
        if output == 13:
            await message.content.send("HOLY SHIT {}! You found a set of waszp foils! But your original foils broke when you tried to fish the waszp foils out.")
            user = message.author.id
            userfile = str(user) + ".txt"
            userfile = str(userfile)
            def replace_line(file_name, line_num, text):
                lines = open(file_name, 'r').readlines()
                lines[line_num] = text
                out = open(file_name, 'w')
                out.writelines(lines)
                out.close()
            replace_line(userfile, 4, "Waszp Foils")
        else:
            newout = random.randint(100, 1000)
            await message.channel.send("You went crusing and some passers-by sponsored you " + str(newout) + " dollars")
            user1 = message.author.id
            userfile1 = str(user1) + ".txt"
            userfile1 = str(userfile1)
            file = open(userfile1, "r")
            lines = file.readlines()
            money = lines[5]
            new_money = str(money) + str(newout)
            def replace_line(file_name, line_num, text):
                lines = open(file_name, 'r').readlines()
                lines[line_num] = text
                out = open(file_name, 'w')
                out.writelines(lines)
                out.close()
            replace_line(userfile1, 5, str(new_money))

client.run(TOKEN2)
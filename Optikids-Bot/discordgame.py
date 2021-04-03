import discord
import os
import time
from discord.errors import InvalidArgument
from discord.ext import commands
from discord.ext.commands.core import cooldown
import random
#ID, Name, Price, Sell, Description
Boats = {
    1: ["Stock used boat", 2000, 250, "A simple, old boat for newbies and noobs who crashed their optis"],
    2: ["The Melting French Optimist", 12000, 2000, "The boat that melts French to win regattas. I mean, you can't be racist against French if there's no French, right?\n Has a chance to be disqualified in races for discrimination"],
    3: ["Far East Optimist", 15000, 4000, "Made in China. Has a chance of dying of COVID-19 BECAUSE THE FACTORY IS LOCATED IN WUUHAN!"],
         }
Spars = {
    1: ["Far East Spars", 4000, 600, "Stock spars from China. Has a chance of breaking"],
    2: ["Black Gold Spars", 8000, 900, "Better spars for beginners"],
    3: ["Optimax MK3", 13000, 100, "Decent shiny spars"]
}
Sails = {
    1: ["Far East Sail", 1000, 10, "The stock sail for beginneer. The only product that is made in China and won't break. Made of cloth"],
    2: ["Olympic Sail", 3000, 1000, "Called an Olympic sail when you can't even watch Opti racing in the Olympics >_^"]
    3: ["J sail Green", 4000, 1600, "The first J sail for lightweight Bri'ish sailors, with Jack Woolterton"]

}
Foils = {
    1: ["Wooden Foils", 1000, 20, "Wooden foils, has a rish of fire"],
    2: ["Plastic Foils", 1500, 60, "Same as wooden foils, just enhanced fire safety"],
    3: ["Far East Foils", 3000, 100, "Finally, some good stuff. Fibre Glass foils! Light, but made in China. Has a risk of breaking"]
}

#boat4
boatname4="Nautivela"
boatprice4 = 18000
boatsell4 = 6000
boatdes4 = "A boat for people who are starting to know what they are doing."
#boat5
boatname5="Blue Blue Optimist"
boatprice5=20000
boatsell5=10000
boatdes5="A boat with a dumbass name but is fast!"
#boat6
boatname6="Winner Optimist"
boatprice6=50000
boatsell6=16000
boatdes6="State-of-the-art optimist made for real winners!! Designed, tested by the legendary Marco Gradoni"

#spars4
sparsname4="Optimax Hyperflex"
sparsprice4=16000
sparssell4=1400
sparsdes4="Spars for you to flex"
#spars5
sparsname5="Optimax Hyped"
sparsprice5=20000
sparssell5=3000
sparsdes5="The spars which everyone is hyped for"
#sail

#sail4
sailname4="J sail Blue"
sailprice4=4300
sailsell4=1800
saildes4="The J sail known to Taiwanese to have a fast acceleration"
#sail5
sailname5="J sail Red"
sailprice5=5000
sailsell5=2000
saildes5="The classic J sail, and the first J sail in the J sail family"
#sail6
sailname6="J sail Black"
sailprice6=5500
sailsell6=2500
saildes6="Originally desgined for heavy sailors. (50+) But, if you can get more power, why not go for it? This game doesn't have stamina stats for players yet."
#sail7
sailname7="OneSail"
sailprice7=6000
sailsell7=2700
saildes7="Newly designed Optimist sail for the pros, and of which Gabriel couldn't afford it during his time in Optimist"
#sail8
sailname8="OneSail Pro"
sailprice8=6500
sailsell8=3000
saildes8="The endgame sail for the best sailors."
#foils
#foils1
foilname1="Wooden foils"
foilprice1=1000
foilsell1=20
foildes1="Wooden foils, has a rish of fire"
#foil2
foilname2="Plastic foils"
foilprice2=1500
foilsell2=60
foildes2="Same as wooden foils, just enhanced fire safety"
#foil3
foilname3="Far East foils"
foilprice3=3000
foilsell3=100
foildes3="Finally, some good stuff. Fibre Glass foils! Light, but made in China. Has a risk of breaking"
#foil4
foilname4="DSK foils"
foilprice4=4000
foilsell4=1200
foildes4="Performance foils for real sailors. Light and thinner for more speed and more life"
#foil5
foilname5="Waszp foils"
foilprice5=10000
foilsell5=4000
foildes5="Not designed for optimists, but you can fly, so why not? Has a chance of tripping over other Optimists or the the anchor line in mark rounding >_^"

#bot stuff
bot = commands.Bot(command_prefix="/")
bot.remove_command('help')
token = "no.nono.noo"
start_time = time.time()
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Bot under restructuring and is broken'))
    print(f'{bot.user.name} has connected to discord and is now online')
    print("Connection time: \n")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("STARTED!!")
@bot.event
async def on_member_join(member):
    await member.create_dm()
    embedVar = discord.Embed(title="Welcome", description="What's up nerd! Don't forget to check out this superior bot! ", color=0xff0000)
    embedVar.add_field(name="Let's get started!", value="Type: (/help) to get started!!", inline=False)
    await member.dm_channel.send(f'Hi {member.name}')
    await member.dn_channel.send(embed=embedVar)
@bot.command(name="ping")
@commands.cooldown(1, 1,commands.BucketType.user)
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
@bot.command(name="shop")
@commands.cooldown(1, 10,commands.BucketType.user)
async def shop(ctx: commands.Context):
    embedVar= discord.Embed(title="Opti Shop!", color = 0xff00ff)
    embedVar.add_field(name="CATEGORY: BOATS", value="1. Stock used boat \n 2. The Melting French Optimist \n 3. Far  East Optimist \n 4. Nautivela \n 5. Blue Blue Optimist \n 6. Winner Optimist", inline=False)
    embedVar.add_field(name="CATEGORY: SPARS", value="1. Far East Spars \n 2. Black Gold Spars \n 3. Optimax Mk3 \n 4. Optimax Hyperflex \n 5. Optimax Hyped", inline=False)
    embedVar.add_field(name="CATEGORY: SAILS", value="1. Far East Sail \n 2. Olympic Sail \n 3. J sail Green \n 4. J sail Blue \n 5. J sail Red \n 6. J sail Black \n 7. OneSail \n 8. OneSail Pro", inline=False)
    embedVar.add_field(name="CATEGORY: FOILS", value="1. Wooden foils \n 2. Plastic foils \n 3. Far East foils \n 4. DSK foils \n 5. Waszp foils", inline=False)
    embedVar.add_field(name="Need more details?", value="Type(/item [category] [itemnumber]) to view the item in details!!") 
    await ctx.send(embed=embedVar)
@bot.command(name="help")
@commands.cooldown(1, 10,commands.BucketType.user)
async def help(ctx: commands.Context):
    embedVar = discord.Embed(title="Guide for OptiKids on discord", description="~Never gonna give you up~", color=0x00fe00)
    embedVar.add_field(name="Start Playing", value="Type: (/createprofile) to create a profile and start playing!! " , inline=True)
    embedVar.add_field(name="View inventionary", value="Type (/invent) to view your inventory", inline=False)
    embedVar.add_field(name="Shop", value="Type (/shop) to view the shop", inline=False)
    embedVar.add_field(name="Cruise", value="Type (/cruise) to start cruising and earn small amounts of money", inline=False)
    embedVar.add_field(name="Updates", value="Type (/update) to check out our newest updates!!")
    embedVar.add_field(name="Source code", value="Type (/source) to view the link to the source code!")
    await ctx.send(embed=embedVar)
@bot.command(name="update")
@commands.cooldown(1, 10,commands.BucketType.user)
async def update(ctx: commands.Context):
    embedVar = discord.Embed(title="Updates", color=0x123456)
    embedVar.add_field(name="Update 1.0", value="Added /cruise command", inline=False)
    embedVar.add_field(name="Update 1.1", value="Minor bug fixes", inline=False)
    embedVar.add_field(name="Update 1.2", value="Minor bug fixes", inline=False)
    embedVar.add_field(name="Update 1.3", value="Minor bug fixes", inline=False)
    embedVar.add_field(name="Update 2.0", value="1. Implemented cooldown for all commands\n2. Code cleanup \n 3. Lowered the cruise successful probability\n 4. Added version checking system (/help) to learn more \n 5. Ram management for server side", inline=False)
    embedVar.add_field(name="You can also type (/todo) to check future updates to be implemented!", value=":)", inline=False)  
    await ctx.send(embed=embedVar)
@bot.command(name="todo")
@commands.cooldown(1, 10,commands.BucketType.user)
async def todo(ctx: commands.Context):
    embedVar = discord.Embed(title = "Todo", color=0x123456)
    embedVar.add_field(name="Todo for update 3.0", value="Allow purchases in shop")
    embedVar.add_field(name="Todo for update 3.1", value="Bug fixes and code cleanup")
    await ctx.send(embed=embedVar)
@bot.command(name="createprofile")
@commands.cooldown(1,10,commands.BucketType.user)
async def create(ctx: commands.Context):
    username = ctx.author.id
    usernamed = str(username) + ".txt"
    str(usernamed)
    existing_users = os.listdir()
    if str(usernamed) in existing_users:
        await ctx.send("{} Your profile exists, don't try to break me.".format(ctx.author.mention))
    else:
        await ctx.send("{} Okay. I am creating your profile now".format(ctx.author.mention))
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
        await ctx.send("{}Done!".format(ctx.author.mention))
@bot.command(name="invent")
@commands.cooldown(1, 3,commands.BucketType.user)
async def invent(ctx: commands.Context):
    await ctx.send("{} Here is your inventory.".format(ctx.author.mention))
    username1 = ctx.author.id
    print(username1)
    usernamed1 = str(username1) + ".txt"
    usernamed1= str(usernamed1)
    name = ctx.author.name
    file = open(usernamed1, "r")
    lines = file.readlines()
    boat = lines[1]
    spars = lines[2]
    sail = lines[3]
    foils = lines[4]
    money = lines[5]
    embedVar = discord.Embed(title=name+"'s inventory", color=0x123456)
    embedVar.add_field(name="Boat", value=boat, inline=True)
    embedVar.add_field(name="Spars", value=spars, inline=True)
    embedVar.add_field(name="Sail", value=sail, inline=True)
    embedVar.add_field(name="Foils", value=foils, inline=True)
    embedVar.add_field(name="Money", value=money,inline=True)
    await ctx.send(embed=embedVar)
@bot.command(name="cruise")
@commands.cooldown(1, 15,commands.BucketType.user)
async def cruise(ctx: commands.Context):
    output = random.randint(1,100)
    if output == 13:
        user = ctx.author.id
        pinger = ctx.author.name
        pinger = str(pinger)
        userfile = str(user) + ".txt"
        userfile = str(userfile)
        def replace_line(file_name, line_num, text):
            lines = open(file_name, 'r').readlines()
            lines[line_num] = text
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
        replace_line(userfile, 4, "Waszp Foils")
        await ctx.channel.send("HOLY SHIT" + pinger +"!"+ "You found a set of waszp foils! But your original foils broke when you tried to fish the waszp foils out.")
    if output > 80:
        kekw = [
            "HAHAHA! Duncan Gregor came to flex on you. He managed to impress some passers-by instead of you! Gain more skills bro",
            "HAHAHA! Alex Dyte full sent his power boat! Make waves and capsizing you. ",
            "HAHAHA! Christos came and took away your sponsored money",
            "No one was impressed. Go gain some skills, loser"
        ]
        hahaha = random.choice(kekw)
        await ctx.channel.send(hahaha)
    if output >60 and output <80 :
        hospital_fees = random.randint(40, 80)
        onofee = str(hospital_fees)
        ono = [
            "HAHAHA! You did a chinese gybe and hit your head! You paid $ " + onofee +  "in hospital fees",
            "HAHAHA! You failed a roll tack and capsized!! You paid the therapist $ " + onofee + "to fix your post capsize horror. What a coward",
            "HAHAHA! Nikita Mazepin decided to drive his yacht! You died! You paid Jesus $ " + onofee + "to respawn yourself. Sorry not sorry"
        ]
        hahahaha = random.choice(ono)
        await ctx.channel.send(hahahaha)
    if output < 59:
        newout = random.randint(100, 200)
        user1 = ctx.author.id
        userfile1 = str(user1) + ".txt"
        userfile1 = str(userfile1)
        file = open(userfile1, "r")
        lines = file.readlines()
        money = lines[5]
        new_money = int(money) + int(newout)
        def replace_line(file_name, line_num, text):
            lines = open(file_name, 'r').readlines()
            lines[line_num] = text + "\n"
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
        replace_line(userfile1, 5, str(new_money))
        await ctx.channel.send("You went cruising and some passers-by sponsored you " + str(newout) + " dollars")
@bot.command(name="source")
@commands.cooldown(1, 5,commands.BucketType.user)
async def source(ctx: commands.Context):
    await ctx.send("Source code: \n https://github.com/nuggetcatsoftware/Optikids-Bot \n Don't forget tp drop a follow to support the devs!!")
@bot.command(name="item")
@commands.cooldown(1, 3, commands.BucketType.user)
async def item(ctx, itemtype, itemnumber):
    if itemtype=="boat":
        if itemnumber=="1":
            boatname = boatname1
            boatprice = boatprice1
            boatsell = boatsell1
            boatdes = boatdes1
        if itemnumber=="2":
            boatname = boatname2
            boatprice = boatprice2
            boatsell = boatsell2
            boatdes = boatdes2
        if itemnumber=="3":
            boatname = boatname3
            boatprice = boatprice3
            boatsell = boatsell3
            boatdes = boatdes3
        if itemnumber=="4":
            boatname = boatname4
            boatprice = boatprice4
            boatsell = boatsell4
            boatdes = boatdes4
        if itemnumber=="5":
            boatname = boatname5
            boatprice = boatprice5
            boatsell = boatsell5
            boatdes = boatdes5
        if itemnumber=="6":
            boatname = boatname6
            boatprice = boatprice6
            boatsell = boatsell6
            boatdes = boatdes6
        embedVar=discord.Embed(title="Shop item", color=0xffff00)
        embedVar.add_field(name=boatname, value="Here you go!", inline=False)
        embedVar.add_field(name="Buy: ", value=boatprice)
        embedVar.add_field(name="Sell: ", value=boatsell, inline=False)
        embedVar.add_field(name="Description: ", value=boatdes, inline=False)
        await ctx.send(embed=embedVar)
    if itemtype=="spars" or itemtype=="spar":
        if itemnumber=="1":
            sparsname = sparsname1
            sparsprice=sparsprice1
            sparssell=sparssell1
            sparsdes=sparsdes1
        if itemnumber=="2":
            sparsname = sparsname2
            sparsprice=sparsprice2
            sparssell=sparssell2
            sparsdes=sparsdes2
        if itemnumber=="3":
            sparsname = sparsname3
            sparsprice=sparsprice3
            sparssell=sparssell3
            sparsdes=sparsdes3
        if itemnumber=="4":
            sparsname = sparsname4
            sparsprice=sparsprice4
            sparssell=sparssell4
            sparsdes=sparsdes4
        if itemnumber=="5":
            sparsname = sparsname5
            sparsprice=sparsprice5
            sparssell=sparssell5
            sparsdes=sparsdes5
        embedVar=discord.Embed(title="Shop item", color=0xffff00)
        embedVar.add_field(name=sparsname, value="Here you go!", inline=False)
        embedVar.add_field(name="Buy: ", value=sparsprice)
        embedVar.add_field(name="Sell: ", value=sparssell, inline=False)
        embedVar.add_field(name="Description: ", value=sparsdes, inline=False)
        await ctx.send(embed=embedVar)
    if itemtype=="sails" or itemtype=="sail":
        if itemnumber=="1":
            sailname=sailname1
            sailprice=sailprice1
            sailsell=sailsell1
            saildes=saildes1
        if itemnumber=="2":
            sailname=sailname2
            sailprice=sailprice2
            sailsell=sailsell2
            saildes=saildes2
        if itemnumber=="3":
            sailname=sailname3
            sailprice=sailprice3
            sailsell=sailsell3
            saildes=saildes3
        if itemnumber=="4":
            sailname=sailname4
            sailprice=sailprice4
            sailsell=sailsell4
            saildes=saildes4
        if itemnumber=="5":
            sailname=sailname5
            sailprice=sailprice5
            sailsell=sailsell5
            saildes=saildes5
        if itemnumber=="6":
            sailname=sailname6
            sailprice=sailprice6
            sailsell=sailsell6
            saildes=saildes6
        if itemnumber=="7":
            sailname=sailname7
            sailprice=sailprice7
            sailsell=sailsell7
            saildes=saildes7
        if itemnumber=="8":
            sailname=sailname8
            sailprice=sailprice8
            sailsell=sailsell8
            saildes=saildes8
        embedVar=discord.Embed(title="Shop item", color=0xffff00)
        embedVar.add_field(name=sailname, value="Here you go!", inline=False)
        embedVar.add_field(name="Buy: ", value=sailprice)
        embedVar.add_field(name="Sell: ", value=sailsell, inline=False)
        embedVar.add_field(name="Description: ", value=saildes, inline=False)
        await ctx.send(embed=embedVar)
    if itemtype=="foils" or itemtype=="foil":
        if itemnumber=="1":
            foilname=foilname1
            foilprice=foilprice1
            foilsell=foilsell1
            foildes=foildes1
        if itemnumber=="2":
            foilname=foilname2
            foilprice=foilprice2
            foilsell=foilsell2
            foildes=foildes2
        if itemnumber=="3":
            foilname=foilname3
            foilprice=foilprice3
            foilsell=foilsell3
            foildes=foildes3
        if itemnumber=="4":
            foilname=foilname4
            foilprice=foilprice4
            foilsell=foilsell4
            foildes=foildes4
        if itemnumber=="5":
            foilname=foilname5
            foilprice=foilprice5
            foilsell=foilsell5
            foildes=foildes5
        embedVar=discord.Embed(title="Shop item", color=0xffff00)
        embedVar.add_field(name=foilname, value="Here you go!", inline=False)
        embedVar.add_field(name="Buy: ", value=foilprice)
        embedVar.add_field(name="Sell: ", value=foilsell, inline=False)
        embedVar.add_field(name="Description: ", value=foildes, inline=False)
        await ctx.send(embed=embedVar)
    else:
        await ctx.send("Listen here you little shit. You have only 1 option; /item [item category] [item number]")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embedVar=discord.Embed(title="Remember. I'm smart enough to detect spam", color=0xff0000)
        embedVar.add_field(name="What a scrub", value=f"Try again after {round(error.retry_after, 2)} seconds!")
        await ctx.send(embed=embedVar)
bot.run(token)


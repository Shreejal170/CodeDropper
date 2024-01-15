import discord
import json
import random
intents = discord.Intents.all()
intents.members = True
from discord.ext import commands
bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

##function to create account for registered members
async def open_account(user):
    users = await get_points()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["points"] = 10
    with open("users.json","w") as f:
        json.dump(users,f)
    return True

async def get_points():
    with open("users.json","r") as f:
        users = json.load(f)
        return users    


async def store_code(code):
    f = open("newcodes.txt", "a")
    f.write(f',{code}')
    f.close()

async def store_expired_code(code):
    f = open("expiredcodes.txt", "a")
    f.write(f',{code}')
    f.close()


async def get_new_codes():
    f = open("newcodes.txt", "r")
    content = f.read()
    f.close()
    list = content.split(",")
    return list

async def get_expired_codes():
    f = open("expiredcodes.txt", "r")
    content = f.read()
    f.close()
    list = content.split(",")
    return list

async def dump_data(data):
    with open('users.json', 'w') as f:
        json.dump(data, f)


async def get_authorized_users():
    with open('config.json', 'r') as f:
        data = json.load(f)
        return data['authorized_users']

async def get_codeDrop_channel():
    with open('config.json', 'r') as f:
        data = json.load(f)
        return data['codedrop_channel']


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')
    print("The bot is ready!")

    

@bot.command()
async def register(ctx):
    user = ctx.author
    users = await get_points()
    if str(ctx.author.id) not in users: 
        await open_account(ctx.author)
        points = users[str(user.id)]["points"]
        embed = discord.Embed(title = f"**{ctx.author.name}**\nYou are registered and your points has been set to {points}",color = discord.Color.green())
        await ctx.send(embed = embed)
        print(f"{ctx.author.name} just registered")
    else:
        ##if user is alredy registered
        await ctx.send("You are already registered.")

@bot.command()
async def gencode(ctx):
    ##gets the list of authorized user's id.
    authorized_users = await get_authorized_users()
    if ctx.author.id in authorized_users:
        code_channel_id = await get_codeDrop_channel()
        channel = bot.get_channel(code_channel_id) ##codes channel
        code = ''.join(random.choice('012345678910') for i in range(10))
        await store_code(code)
        await channel.send(f"{code}")
    else:
        print(f"{ctx.author.name} tried to print")
        await ctx.send("https://tenor.com/view/no-nooo-nope-eat-fingerwag-gif-14832139")


@bot.command()
async def redeem(ctx, code):
    user = ctx.author
    users = await get_points()
    newcodes = await get_new_codes()
    expired_codes = await get_expired_codes()
    try:
        if code in expired_codes:
            await ctx.send("```The code has expried :(```")
        elif code in newcodes:
            users[str(user.id)]["points"] += 5
            await dump_data(users)
            points = users[str(user.id)]["points"]
            await ctx.send(f"```Code has been redeemed.Now your point is: {points}```")
            await store_expired_code(code)
        else:
            await ctx.send("```CODE IS INVALID```")
    except:
        await ctx.send("You have to register first using command: `$register`")


bot.run("MTE1MTM2NzA2MTkzNTc2MzQ1Nw.GGWfjH.osllL0pD67zDYwcIGEZnuW6F0pue37YEoiSW-I")
    
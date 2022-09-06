import discord
from discord.ext import commands
import random
from botcommandvariables import *
from tarotcards import *
from tarotinfo import *
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '$', intents = intents)
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for $how'))
    
@bot.event

async def on_message(message):
    if message.content.lower() == "hello":
        await message.channel.send(f"Hello, {message.author.mention}!")
    if message.content.lower() == 'goodbye':
        await message.channel.send(f'Nice hangin out, {message.author.mention}! Buh byyyyyyye!')
    if 'wtf' in message.content.lower():
        await message.channel.send('what the faz*fuck*, indeed, fazfam.')
    if message.content.lower() =='bros':
        await message.channel.send('fazfam')
    if message.content.lower() == 'gg':
        await message.channel.send(f'GG, {message.author.mention}!')
    if message.content.lower() == 'i love you fazbot' or message.content.lower() == 'i love fazbot' or message.content.lower() =='fabzot i love you':
        await message.channel.send(f'Aww, I love you, too {message.author.mention}.')
    # if message.content.startswith('$cheers') or message.content.startswith('!cheers') == True:
    #     with open('secret.txt', 'a') as file:
    #         file.write(f'another drink logged by {message.author} in {message.guild} \n')
    #     with open('secret.txt') as file:
    #         print(file.read())  
    #     await message.channel.send(f'Another one for {message.author.mention}...')
    # if '$drunk' in message.content or '$drinks' in message.content or '!drunk' in message.content or '!drinks' in message.content:
    #     with open('secret.txt') as file:
    #         drinks = len(file.readlines()) 
    #     await message.channel.send(f'the server has had {drinks} drinks so far!')
    # if message.content.startswith('!closingtime') or message.content.startswith('$closingtime') == True:
    #     with open('secret.txt', 'r') as infile, open ('secretmaster.txt', 'a') as outfile:
    #         outfile.write(str(infile.readlines()))
    #     with open('secret.txt', 'w') as file:
    #         file.write('')
    #     await message.channel.send(f'{message.author.mention} has cleared the tracker! Time to refill it!')
    await bot.process_commands(message)
@bot.command(pass_context = True,
    help = 'get the guild ID for the server the bot is on',
    brief = 'get guild ID information for the server'
)
async def serverid(ctx):
    id = ctx.message.guild.id
    await ctx.message.send(id)
@bot.command(
	# ADDS THIS VALUE TO THE $HELP PING MESSAGE.
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send("pong")
@bot.command(
    help='more crazy logic for pong this time.',
    brief='prints ping to the channel'
)
async def pong(ctx):
    await ctx.channel.send('ping')
@bot.command(pass_context = True, 
    help='picks a random joke by doing some math. I never said they would be good.',
    brief='fazbot will tell you a joke.'
)
async def joke(ctx):
    jokes_copy = jokes.copy()
    rj = random.choice(jokes_copy)
    jokes_copy = jokes_copy.remove(rj)
    await ctx.channel.send(rj)
@bot.command(
    help='posts a picture of the OG fazdad',
    brief='for when you want a picture of freddy'
)    
async def freddy(ctx):
    freddyfotos_copy = freddyfotos.copy()
    rff = random.choice(freddyfotos_copy)
    freddyfotos_copy = freddyfotos_copy.remove(rff)
    await ctx.channel.send(rff)
@bot.command(
    help='post a picture of chica',
    brief='for when you wanna look at a pizza obsessed chicken(or maybe markiplier\'s dog?)'
)
async def chica(ctx):
    chicafotos_copy = chicafotos.copy()
    rcf = random.choice(chicafotos_copy)
    chicafotos_copy = chicafotos_copy.remove(rcf)
    await ctx.channel.send(rcf)
@bot.command(
    help='posts a picture of foxy',
    brief='I feel like you should understand this at this point.'
)
async def foxy(ctx):
    foxyfotos_copy = foxyfotos.copy()
    rfx = random.choice(foxyfotos_copy)
    foxyfotos_copy = foxyfotos_copy.remove(rfx)
    await ctx.channel.send(rfx)
@bot.command(
    help='posts a picture of bonnie',
    brief='Bonnie the bunny. From FNAF. As a photo.'
)
async def bonnie(ctx):
    bonniefotos_copy = bonniefotos.copy()
    rbf = random.choice(bonniefotos_copy)
    bonniefotos_copy = bonniefotos_copy.remove(rbf)
    await ctx.channel.send(rbf)
@bot.command(
    help='posts a photo from the fnaf/afton nonsense.',
    brief='fnaf + afton = fnafton or something.'
)
async def fnafton(ctx):
    fnaftonfotos_copy = fnaftonfotos.copy()
    rfa = random.choice(fnaftonfotos_copy)
    fnaftonfotos_copy = fnaftonfotos_copy.remove(rfa)
    await ctx.channel.send(rfa)
@bot.command(
    help='this posts my good morning message because fazdad is fazforgetful.',
    brief='a daily reminder for yous'
)
async def morning(ctx):
    await ctx.channel.send('Good morning, my faztastic ~~followers~~ friends! Here is your reminder to hydrate, medicate, masticate, and meditate!')
@bot.command(
    help='jim',
    brief="Jim."
)
async def jim(ctx):
    jim_copy = jimfotos.copy()
    randomjim = random.choice(jim_copy)
    jim_copy = jim_copy.remove(randomjim)
    await ctx.channel.send(randomjim)
@bot.command(
    help = 'log a drink! a dab! a glass of water! The world is yours for the taking!',
    brief = 'keep track of your substance intake however you see fit.'
)
async def cheers(ctx):
    cheersmessages_copy = cheersmessages.copy()
    randomcheers = random.choice(cheersmessages_copy)
    cheersmessages_copy = cheersmessages_copy.remove(randomcheers)
    serverid = ctx.message.guild.id
    with open(f'drinklog{serverid}.txt', 'a') as log:
        log.write(f'another drink logged by {ctx.message.author} in {ctx.message.guild} \n')
        await ctx.channel.send(randomcheers)
@bot.command(
    help = 'this gives the total "drinks" had in the server since the last time the log was cleared',
    brief = 'how much has the server had? fazbot can and will tell you.'
)
async def drinks(ctx):
    serverid = ctx.message.guild.id
    with open(f'drinklog{serverid}.txt') as log:
        drinks = len(log.readlines())
    await ctx.channel.send(f'{ctx.message.guild} has had {drinks} drinks(wink wonk wink) so far! Leggo.')
@bot.command(
    help = 'this will show you how many drinks *you* have had in the server you use the command in',
    brief = 'how much have you had? find out here!'
)
async def drunk(ctx):
    serverid = ctx.message.guild.id
    member = ctx.message.author
    with open(f'memberlog{member}.txt', 'w') as tracker:
        tracker.write('')
    with open (f'drinklog{serverid}.txt') as file, open(f'memberlog{member}.txt', 'a') as tracker:
        for line in file.readlines():
            if str(member) in line:
                tracker.write(line)
    with open(f'memberlog{member}.txt') as log:
        memberdrinkcount = len(log.readlines())
    await ctx.channel.send(f'You have had {memberdrinkcount} drinks(wink wonk) so far, {ctx.message.author.mention}')
@bot.command(
    help = 'clears the server drink log',
    brief = 'start the drinking over from 0!'
)
async def closingtime(ctx):
    serverid = ctx.message.guild.id
    member = []
    member.append(member for members in ctx.message.guild.members)
    with open(f'drinklog{serverid}.txt', 'r') as infile, open ('secretmaster.txt', 'a') as outfile:
        outfile.write(str(infile.readlines()))
    with open(f'drinklog{serverid}.txt', 'w') as file:
        file.write('')
    await ctx.channel.send(f'{ctx.message.author.mention} has cleared the tracker for {ctx.message.guild}! Time to refill it!')
@bot.command(
    help = 'this just tells you how to use the bot kinda sorta',
    brief = 'how does this thing work, anyway?'
)
async def how(ctx):
    with open('secret.txt') as help:
        helplist = ''
        for line in help.readlines():
            helplist = helplist + line
    await ctx.channel.send(f' Here you go, {ctx.message.author.mention} : {helplist}')
# @bot.command()
# async def tarot(ctx):
#     await ctx.channel.send(tarot_reader())

bot.run('TOKEN')

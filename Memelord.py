import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import sys
import time

Client = discord.Client()
bot_prefix= ","
client = commands.Bot(command_prefix=bot_prefix)

luke_say = ["nyarr, you're a pansey","nyarr horseburg", "shank shank","nyarr, lunchboy","your a communist"]
billy_say = ["im smarter than you so your wrong","your fat","im stupid",
"i have more friends than you","i should be in grandmasters","i main junkrat"]
memes = ["Finger food isn't fingers they said, you just eat it with your fingers, so it's called finger food! But they couldn't trick me like that, " \
"underneath the crisps and the pretzels and the nuts and the raisins I could see fingers, hundreds and hundreds of fingers wiggling about whispering eat me, eat me, eat me.",
"https://cdn.discordapp.com/attachments/370727786865754117/375043710167023616/552x414bb.png"
,"https://cdn.discordapp.com/attachments/370727786865754117/377500021894938624/tenor.gif"
,"https://cdn.discordapp.com/attachments/356163365825150977/374571601192026123/c2wAAAABJRU5ErkJggg.png"
,"https://giphy.com/gifs/u--je-P4mzY1dEJg8Ew"
,"https://youtu.be/xMlT_8jm-0E"
,'https://cdn.discordapp.com/attachments/336614631755743234/384825419628544016/maxresdefault.png']
comp = ["6M HCL","Don't trust atoms. They make up everything",'18 MH2SO4',"Can we blow something up today?","Did you know that you can cool yourself to -273˚C and still be 0K?"]
compy = ["Debbie used to drink in the lab\nBut now she drinks no more\nFor what she thought was H2O\nWas H2SO4"
,"Debbie used to breathe in the lab\nBut now she breathes no more\nFor what she thought was O2 gas\nHad a higher molar mass"]
monname = ['The MemoryHead','The goblin','The ChainChomp','Debbie','The Hammer Bro.','The pufferfish','The 6M HCl','The Calc King','The Hacker Bot'
,'The Genji main','The pansey','The ghost pirate','Donald Trump','Hillary Clinton','Bernie Sanders','Kim Jong-Un']
currentmon = monname[random.randint(0,len(monname))]
wont = ['I refuse.',"don't feel like it",'please no',"but EFFORT..."]
greetings = ['hello!','salutations!','heyo!']
HP = random.randint(5000,10000)
owner = '335958571533598721'

        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.command(pass_context=True)
async def play(ctx, game = None):
    if ctx.message.author.id == owner :
        if game is None:
            game = 'type ,help'
        await client.change_presence(game=discord.Game(name='{0}'.format(game)))
        await client.say("done!")
    else :
        await client.say(wont[random.randint(0,4)])
        
@client.command(pass_context=True)
async def luke (ctx):
    time.sleep(0.3)
    await client.say(luke_say[random.randint(0,5)])
    
@client.command(pass_context=True)  
async def billy (ctx):
    time.sleep(0.3)
    await client.say(billy_say[random.randint(0,6)])
        
@client.command(pass_context=True)
async def kek (ctx):
    time.sleep(0.3)     
    await client.say("kekekekekekekekekekekekekekekekekekekekekekekekekekekekekekekekek",tts=True)

@client.command(pass_context=True)
async def gengu (ctx):
    time.sleep(0.8) 
    await client.say("7 upvotes")
    time.sleep(0.8)
    await client.say("31 elims")
    time.sleep(0.8)
    await client.say("and play")
    time.sleep(1)
    await client.say("am i a good gengu now (yes/no)")
    ans = await client.wait_for_message(timeout=None, author=ctx.message.author, check=None)
    if ans.content == "yes" :
        await client.say("thank you")
    elif ans.content == "no" :
        await client.say("screw you")
    else :
        await client.say("thats not an answer")

@client.command(pass_context=True)
async def kai (ctx):
    time.sleep(0.3)     
    await client.say("https://cdn.discordapp.com/attachments/360576264769241098/378665756373811201/Screenshot_2017-11-10-14-11-42-1.png")
    
@client.command(pass_context=True)
async def hit (ctx):
    global HP
    global currentmon
    if ctx.message.author.id == owner :
        damage = random.randrange(500,800)
    else :
        damage = random.randrange(100,500)
    HP -= damage
    if HP > 0 :
        await client.say(currentmon + ' took ' + str(damage) + ' damage and has ' + str(HP) + ' health left.')
    else :
        await client.say(currentmon + ' has been defeated!')
        currentmon = monname[random.randint(0,len(monname))]
        await client.say(currentmon + ' approaches!')
        HP = random.randint(1000,5000)
    
@client.command(pass_context=True)
async def rice (ctx):
    for x in range(0, 10):
        time.sleep(0.5)
        await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")

@client.command(pass_context=True)
async def nou (ctx):
    for x in range(0, 10):
        time.sleep(0.5)
        await client.say("no u", tts=True)
        

@client.command(pass_context=True)  
async def dave (ctx):
    time.sleep(0.3)
    await client.say("Dave is a unibrow frog with no friends")
        
@client.command(pass_context=True)  
async def anish (ctx):
    time.sleep(0.3)
    await client.say("oi yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

@client.command(pass_context=True)
async def mario (ctx):
    time.sleep(0.3)
    await client.say("── ── ── ── ── ── ── ██ ██ ██ ██ ── ██ ██ ██ ── \n── ── ── ── ── ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ \n── ── ── ── ██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ \n" \
"── ── ── ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ░░ ░░ ██ \n── ── ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ░░ ██ \n── ── ██ ▓▓ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ ── \n" \
"── ██ ██ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██ \n── ██ ░░ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██ \n██ ░░ ░░ ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ \n" \
"██ ░░ ░░ ░░ ██ ░░ ░░ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ \n── ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ░░ ░░ ██ ██ ██ ── \n── ── ██ ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ██ ▓▓ ██ ── \n" \
"── ── ── ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ▓▓ ██ ── \n── ── ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ▓▓ ██ ── ── \n── ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ ██ ── ── ── \n" \
"██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██ ── ── ── \n██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██ ── ── ── \n██ ██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ ██ ██ ██ ── \n" \
"── ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ── \n── ── ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ██ \n── ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ \n" \
"██ ██ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ \n██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ \n██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ── ── ── ██ ▓▓ ▓▓ ██ ██ \n" \
"██ ▓▓ ▓▓ ██ ██ ── ── ── ── ── ── ── ██ ██ ██ ── \n── ██ ██ ── ── ── ── ── ── ── ── ── ── ── ── ──﻿")
    
@client.command(pass_context=True)  
async def meme (ctx):
    time.sleep(0.3)
    await client.say(memes[random.randint(0,7)])
    
@client.command(pass_context=True)  
async def chem (ctx):
    time.sleep(0.3)
    if random.randint(0,10)==10 :
        await client.say(compy[random.randint(0,2)])
    else :
        await client.say(comp[random.randint(0,5)])

client.run("MzcxMTA2NzMxNTc0Njg5ODAz.DMwzlg.d7auDagAQ05Iv7lCG2HESJg-nWs")

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import sys
import os

Client = discord.Client()
bot_prefix= ","
client = commands.Bot(command_prefix=bot_prefix)

luke_say = ["nerr, you're a pansey","nerr horseburg", "shank shank","nerr, lunchboy","your a communist"]
billy_say = ["im smarter than you so your wrong","your fat","im stupid","i have more friends than you","i should be in grandmasters","i main junkrat"]
boi = ["https://cdn.discordapp.com/attachments/370727786865754117/375039491410362369/28e.png"]
boi.extend(["https://cdn.discordapp.com/attachments/370727786865754117/375043710167023616/552x414bb.png"])
boi.extend(["https://cdn.discordapp.com/attachments/370727786865754117/375043295031853056/flat800x800075t.png"])

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='as Junkrat'))
	print("Bot Online!")

@client.command(pass_context=True)
async def command (ctx):
	await client.say(",nou ,anish ,kek ,luke ,billy ,datboi ,rice")

@client.command(pass_context=True)
async def luke (ctx):
	await client.say(luke_say[random.randrange(0,5)])

@client.command(pass_context=True)	
async def billy (ctx):
	await client.say(billy_say[random.randrange(0,6)])
	
@client.command(pass_context=True)
async def nou (ctx):
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")
	await client.say("no u")

@client.command(pass_context=True)
async def kek (ctx):
	await client.say("kekekekekekekekekekekekekekekekekekekekekekekekekekekekekekekekek")
	
@client.command(pass_context=True)
async def rice (ctx):
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")
	await client.say(":rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball::rice_ball:")

@client.command(pass_context=True)	
async def anish (ctx):
	await client.say("oi yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
	
@client.command(pass_context=True)	
async def datboi (ctx):
	await client.say(boi[random.randrange(0,len(boi))])

client.run("MzcxMTA2NzMxNTc0Njg5ODAz.DMwzlg.d7auDagAQ05Iv7lCG2HESJg-nWs")

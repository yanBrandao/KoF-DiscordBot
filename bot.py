# KoF DiscordBot by yanbrandao

import asyncio
import discord
import chalk
from discord.ext import commands
from discord.ext.commands import Bot



bot = commands.Bot(command_prefix="#")


@bot.event
async def on_ready():
	print("Ready when you are xD")
	print("I am running on " + bot.user.name)
	print("With the ID: " + bot.user.id)

@bot.event
async def on_member_update(before, after):
	playerGame = discord.Member.game
	if playerGame:
		print("Está jogando" + str(playerGame))

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say(":ping_pong: pong you bastard!")
	print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	title = "KoF Ranking - {}".format(user.name)
	info = discord.Embed(title=title, description="DiscordBot Ranking", color=0x00ff00)
	info.set_footer(text="Most Character played: ".format(user.status))
	info.set_author(name="Teste of Author")
	info.add_field(name="This is a field", value="no it isn't", inline=True)
	await bot.say(embed=info)
	print("{} was checked".format(user.name))



bot.run("NDM2NzMzMjg3NjU5MjA4NzEy.DbsKTg.aHBJh8_eapGtLNBCv_84rw1lirQ")
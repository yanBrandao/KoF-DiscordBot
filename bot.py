# KoF DiscordBot by yanbrandao

import asyncio
import discord
import chalk
import psycopg2
import time



from DBConnection import *
from discord.ext import commands
from discord.ext.commands import Bot


userConnect = { '_init_': -1}
bot = commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
	print("Ready when you are xD")
	print("I am running on " + bot.user.name)
	print("With the ID: " + bot.user.id)

@bot.event
async def on_member_update(before, after):
		print('{0.nick} encerrou {0.game}'.format(before))
		game = '{0.game}'.format(after)
		nick = '{0.nick}'.format(after)
		print('{0.nick} iniciou {0.game}'.format(after))
		if game != 'None':
			userConnect[nick] = time.time()
			print(userConnect)
		game = '{0.game}'.format(before)
		nick = '{0.nick}'.format(before)
		if game != 'None':
			timeSpend = time.time() - userConnect[nick]
			userConnect.__delitem__(nick)
			print(timeSpend)

@bot.event
async def on_voice_state_update(before, after):
    if before is not None:
        user = before or after
        print('{0.name} entrou do Canal {0.voice.voice_channel.name}'.format(user))


@bot.command(pass_context=True)
async def entrar(self, member: discord.Member):
    user = discord.User

    con = DBConnection()
    sql = 'INSERT INTO public.player(nickname, victories, defeats, country, "discordUser") VALUES (\'{0.name}\', 0, 0, \'{0.server.region}\',\'{0.id}\');'.format(member)
    print(sql)
    if(con.changeDatabase(sql)):
       await bot.say("Jogador inserido com sucesso ao rank :muscle:")
    else:
        await bot.say("Você já foi adicionado ao ranking! :rolling_eyes:")
    


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



@bot.command(pass_context=True)
async def duelo(ctx, user: discord.Member):
    
    playerOne = '{0.name}'.format(ctx.message.author)
    print(playerOne)
    playerTwo = '{0.name}'.format(user)
    myServer = ctx.message.server
    await bot.create_channel(myServer, playerOne + ' vs. ' + playerTwo, type=discord.ChannelType.voice)
    newBotChannel = 0
    for channels in myServer.channels:
        if (channels.name == playerOne + ' vs. ' + playerTwo):
            print('Found '+ playerOne + ' vs. ' + playerTwo + ' channel. :D')
            newBotChannel = channels
    await bot.move_member(user, newBotChannel)
    await bot.move_member(ctx.message.author, newBotChannel)
    await bot.say('Lutem!')






bot.run("NDM2NzMzMjg3NjU5MjA4NzEy.DbsKTg.aHBJh8_eapGtLNBCv_84rw1lirQ")
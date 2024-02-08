#!/usr/bin/python3
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents(8)
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

#@bot.event
#async def on_ready():
#	guild = discord.utils.get(bot.guilds, name=GUILD)
#	print(
#		f'{bot.user.name} is connected to:\n'
#		f'{guild.name}(id: {guild.id})'
#	)

@bot.command(name='list')
async def command_list(ctx):
	await ctx.send('under development')

bot.run(TOKEN)
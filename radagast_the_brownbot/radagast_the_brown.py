#!/usr/bin/python3
import os
import subprocess
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)

#@bot.event
#async def on_ready():
#    guild = discord.utils.get(bot.guilds, name=GUILD)
#    print(
#        f'{bot.user.name} is connected to:\n'
#        f'{guild.name}(id: {guild.id})'
#    )

@bot.command(name='gul')
async def command_list(ctx):
    await ctx.send('Ash nazg durbatuluk, ash nazg gimbatul, '
                   'ash nazg thrakatuluk, agh burzum-ishi '
                   'krimpatul.')

bot.run(TOKEN)
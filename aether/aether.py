#!/usr/bin/python3
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def hi(ctx):
    await ctx.send('i like poop')

bot.run(TOKEN)
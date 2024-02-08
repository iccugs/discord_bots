#!/usr/bin/python3
import os
import subprocess
import discord
from pathlib import *
import os.path
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MAIGRETDIR = os.getenv('MAIGRET_DIRECTORY')
DPDIR = os.getenv('DISCORDPURGE_DIRECTORY')
OGRAM = os.getenv('OSINTGRAM_DIRECTORY')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
bot.remove_command('help')

@bot.command()
async def help(ctx, cmd=None):
    if not cmd:
        await ctx.send(
            'commands:\n\n'
            'uscan - (username scan)\n'
            'usfile - (upload uscan file from cache)\n'
            'uscache - (print uscan cache)\n'
            'usclear - (uscan clear cache)\n'
            'emscan - (still in development)\n'
            'pscan - (port scan)\n'
            'pfile - (upload pscan file from cache)\n'
            'pcache - (print pscan cache)\n'
            'pclear - (pscan clear cache)\n'
            'tscrape - (still in development)\n'
            'igscrape - (igscrape still in development)\n'
            'purge - (still in development)\n'
            'iplog - (still in development)\n'
            'pws - (still in development)\n'
            'botnet - (still in development)\n\n'
            'type !help \{command\} for help on that topic'
        )
    elif cmd.lower()=="uscan":
        await ctx.send("type '!uscan \{username\}' to use Maigret to scan the top 2500 websites for matches")
    elif cmd.lower()=="usfile":
        await ctx.send("type '!usfile \{filename\}' to upload a Maigret report pdf from the uscan cache")
    elif cmd.lower()=="uscache":
        await ctx.send("type '!uscache' to list all files currently in the uscan cache folder")
    elif cmd.lower()=="usclear":
        await ctx.send("type '!usclear' to clear all files currently in the uscan cache folder")
    elif cmd.lower()=="emscan":
        await ctx.send("still in development")
    elif cmd.lower()=="pscan":
        await ctx.send("type '!pscan \{ipv4 address\}' to do an intense verbose pingless syn stealth nmap scan of the target IP (will also accept a CIDR IP range by typing !pscan \{ipv4 address\}/\{CIDR notation\})")
    elif cmd.lower()=="pfile":
        await ctx.send("type '!pfile \{filename\}' to upload a nmap scan report from the nmap report cache")
    elif cmd.lower()=="pcache":
        await ctx.send("type '!pcache' to list all files currently in the pscan cache folder")
    elif cmd.lower()=="pclear":
        await ctx.send("type '!pclear' to clear all files currently in the pscan cache folder")
    elif cmd.lower()=="tscrape":
        await ctx.send('still in development')
    elif cmd.lower()=="igscrape":
        await ctx.send('still in development')
    elif cmd.lower()=="purge":
        await ctx.send('still in development')
        #await ctx.send("type '!purge \{discord token\} \{name#tag\}' to delete all messages that were sent to a DM chat with any given user#tag")
    elif cmd.lower()=="iplog":
        await ctx.send('still in development')
    elif cmd.lower()=="pws":
        await ctx.send('still in development')
    elif cmd.lower()=="bnet":
        await ctx.send('still in development')
    else:
        await ctx.send('invalid option')

@bot.command(name='uscan')
async def maigret_script(ctx, arg):
    await ctx.send('scanning...')
    subprocess.run([f'{MAIGRETDIR}/venv/bin/python3',f'{MAIGRETDIR}/maigret.py','-a',arg,'--pdf'],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    usOut = discord.File(f'reports/report_{arg}.pdf')
    await ctx.send(file=usOut, content='scan complete!')

@bot.command(name='usfile')
async def usfile_upload(ctx, arg):
    usFile = discord.File(f'reports/{arg}')
    await ctx.send(file=usFile, content='file uploaded!')

@bot.command(name='uscache')
async def uscache_print(ctx):
    usCache = subprocess.run(['ls','-l','reports/'],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    await ctx.send(usCache.stdout)

@bot.command(name='usclear')
async def uscache_clear(ctx):
    subprocess.run(['rm','-rf','reports/'],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    subprocess.run(['mkdir','reports'],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    await ctx.send('cleared!')

@bot.command(name='emscan')
async def instagram_scrape(ctx):
    await ctx.send('still in development')

@bot.command(name='pscan')
async def nmap_script(ctx, arg):
    await ctx.send('scanning...')
    pscanOut = subprocess.Popen(['nmap','-p-','-sV','sC',arg,'--open'],stderr=subprocess.PIPE, universal_newlines=True,stdout=subprocess.PIPE)
    pscanTee = subprocess.Popen(['tee', f'nmapscans/{arg}.txt'], stdin=pscanOut.stdout, stdout=subprocess.PIPE)
    pscanComplete = pscanTee.communicate()
    print(pscanComplete)
    nmapOut = discord.File(f'nmapscans/{arg}.txt')
    await ctx.send(file=nmapOut, content='scan complete!')

@bot.command(name='pfile')
async def pfile_upload(ctx, arg):
    pFile = discord.File(f'nmapscans/{arg}')
    await ctx.send(file=pFile, content='file uploaded!')

@bot.command(name='pcache')
async def pcache_print(ctx):
    pCache = subprocess.run(['ls','-l','nmapscans/'],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    await ctx.send(pCache.stdout)

@bot.command(name='pclear')
async def pcache_clear(ctx):
    subprocess.run(['rm','-rf','nmapscans/'],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    subprocess.run(['mkdir','nmapscans'],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    await ctx.send('cleared!')

@bot.command(name='tscrape')
async def twitter_scrape(ctx):
    await ctx.send('still in development')

@bot.command(name='igscrape')
async def instagram_scrape(ctx):
    await ctx.send('still in development')

@bot.command(name='purge')
async def discordpurge_script(ctx):
    await ctx.send('still in development')
#async def discordpurge_script(ctx, arg1, arg2):
    #purgeOut = subprocess.Popen(['echo', arg1], stderr=subprocess.PIPE, universal_newlines=True, stdout=subprocess.PIPE)
    #purgeTee = subprocess.Popen(['sudo', 'tee', f'{DPDIR}/auth_token.txt'], stdin=purgeOut.stdout, stdout=subprocess.PIPE)
    #purgeComplete = purgeTee.communicate()
    #print(purgeComplete)
    #subprocess.run([f'{DPDIR}/venv/bin/python3', f'{DPDIR}/discordpurge.py', '-q', arg2], check=True, stdout=subprocess.PIPE, universal_newlines=True)
    #subprocess.run(['rm', '-f', f'{DPDIR}/auth_token.txt'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
    #await ctx.send('purge complete!')

@bot.command(name='iplog')
async def iplogger_script(ctx):
    await ctx.send('still in development')

@bot.command(name='pws')
async def passwordscrape_script(ctx):
    await ctx.send('still in development')

@bot.command(name='bnet')
async def ddos_script(ctx):
    await ctx.send('still in development')

bot.run(TOKEN)

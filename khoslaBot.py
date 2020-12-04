# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='kh ')

#bot online
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})' 
    )

#confessions
@bot.command(name = 'confess', help = 'DM me a confession!')
async def on_message(ctx):
    confession = ctx.message.content[11:len(ctx.message.content)]
    if ctx.author == bot.user:
        return
    if not ctx.guild:
        await ctx.channel.send('Confession submitted!')
        confessionApproval = bot.get_channel(784308011656675358)
        await confessionApproval.send(confession)

bot.run(TOKEN)

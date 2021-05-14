# bot.py
import os
# import random
import discord
import confessions

# from discord.ext import commands
from dotenv import load_dotenv
import config as c
import sql as db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
SQLITEFILE = os.getenv('SQLITE_FILE')

# bot online


@c.bot.event
async def on_ready():
    print(f'{c.bot.user.name} has connected to Discord!')
    db.init(SQLITEFILE)

    guild = discord.utils.get(c.bot.guilds, name=GUILD)
    print(
        f'{c.bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    async for guild in c.bot.fetch_guilds(limit=150):
        print(guild.name)


@c.bot.command(name='ping', help='Test')  # is bot alive
async def on_message(ctx):
    await ctx.channel.send('Pong!')

c.bot.run(TOKEN)

#test commit

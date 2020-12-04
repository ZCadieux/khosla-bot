"""import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv"""
import config as c

# confessions


@c.bot.command(name='confess', help='DM me a confession!')
async def on_message(ctx):
    confession = ctx.message.content[11:len(ctx.message.content)]
    if ctx.author == c.bot.user:
        return
    if not ctx.guild:
        await ctx.channel.send('Confession submitted!')
        confessionApproval = c.bot.get_channel(784308011656675358)
        await confessionApproval.send(confession)

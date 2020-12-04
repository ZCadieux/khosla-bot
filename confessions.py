import os
# import random
# import discord

# from discord.ext import commands
# from dotenv import load_dotenv
import config as c


COUNT = os.path.expanduser("~\\Documents\\GitHub\\khosla-bot\\count.txt")


def updateConfNum(newConfNum):
    with open(COUNT, "w") as fd:
        fd.write(str(newConfNum) + "\n")


def retrieveConfNum():
    with open(COUNT, "r") as fd:
        return fd.readline().strip()

# confessions


@c.bot.command(name='confess', help='DM me a confession!')
async def on_message(ctx):
    confession = ctx.message.content[11:len(ctx.message.content)]
    if ctx.author == c.bot.user:
        return
    if not ctx.guild:
        confNum = 1 + int(retrieveConfNum())
        confText = f'Confession Number {confNum} submitted!'
        await ctx.channel.send(confText)
        confessionApproval = c.bot.get_channel(784308011656675358)
        updateConfNum(confNum)
        await confessionApproval.send(confession)

import os
# import random
# import discord

# from discord.ext import commands
# from dotenv import load_dotenv
import config as c
import sql as db


COUNT = os.path.expanduser("~\\Documents\\GitHub\\khosla-bot\\count.txt")


def updateConfNum(newConfNum):
    with open(COUNT, "w") as fd:
        fd.write(str(newConfNum) + "\n")


def retrieveConfNum():
    with open(COUNT, "r") as fd:
        return fd.readline().strip()

# confessions


@c.bot.command(name='confess', help='DM me a confession!')  # recieve confessions
async def on_message(ctx):
    confession = ctx.message.content[11:len(ctx.message.content)]
    if ctx.author == c.bot.user:
        return
    if not ctx.guild:
        # confessionApproval = c.bot.get_channel(784308011656675358)
        # await confessionApproval.send(confession)
        # if successfully confessed,since confess returns the message id
        queued = db.confess(confession)
        if queued is not None:
            confText = f'Confession Number {retrieveConfNum()} submitted!'
            await ctx.channel.send(confText)
            await c.bot.add_reaction(queued, 'thumbsup')
            await c.bot.add_reaction(queued, 'thumbsdown')


@c.bot.event  # reactions in queue
async def on_raw_reaction_add(payload):
    if db.isQueuedConfession(payload.message_id) is not True:
        return
    if payload.event_type != 'REACTION_ADD' and payload.user_id != 784307745918025739:  # don't trigger on own react
        if payload.emoji == 'thumbsup':
            db.approve(payload.message_id)
        if payload.emoji == 'thumbsdown':
            db.deny(payload.message_id)

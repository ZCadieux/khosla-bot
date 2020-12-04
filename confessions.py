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

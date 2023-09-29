import hikari
import lightbulb

import random

plugin = lightbulb.Plugin('command')


# example of command
@plugin.command
@lightbulb.command('ping', 'checks the bot is alive')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):

    await ctx.respond("Pong!")


# roll number from min and max input
@plugin.command
# use string to check with isnumeric() function
@lightbulb.option('num2', 'The second number', type=str)
@lightbulb.option('num1', 'The first number', type=str)
@lightbulb.command('random', 'roll number')
@lightbulb.implements(lightbulb.SlashCommand)
async def rannum(ctx):

    if ctx.options.num1.isnumeric() and ctx.options.num2.isnumeric():
        num1 = int(ctx.options.num1)
        num2 = int(ctx.options.num2)
        anws = str(random.randint(num1, num2))

        await ctx.respond(anws)
    else:
        await ctx.respond('Please use number as input')


def load(bot):
    bot.add_plugin(plugin)

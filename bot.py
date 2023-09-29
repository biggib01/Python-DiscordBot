import discord
import responses
import random

from discord.ext import commands

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    # openai.api_key = "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"
    TOKEN = 'OTEwOTUzNTk4MDg1NjQ0Mjg4.GFSLuC.5Cf3o9qUl0yiods2alTpmtkg7KktbxZXPbumLc'
    intents = discord.Intents.default()
    intents.message_content = True
    # client = discord.Client(intents=intents)

    client = commands.Bot(command_prefix='#', intents=intents)

    @client.command()
    async def foo(ctx, arg):

        print(arg)
        await ctx.send(arg)

    @client.command()
    async def anime(ctx):

        print()
        await ctx.send()

    @client.command()
    async def roll(ctx, arg1, arg2):

        if arg1.isnumeric() and arg2.isnumeric():
            num1 = int(arg1)
            num2 = int(arg2)
            anws = str(random.randint(num1, num2))

            print(anws)
            await ctx.reply(anws)
        else :
            await ctx.reply('Please use number as input')

    @client.event
    async def on_ready():
        print(f'{client.user} is no running!')

    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return
    #
    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)
    #
    #     print(f'{username} said: "{user_message}" ({channel})')

        # if user_message[0] == '?':
        #     user_message = user_message[1]
        #     await send_message(message, user_message, is_private=True)
        # else:
        #     await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
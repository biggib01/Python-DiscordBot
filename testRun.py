import hikari
import lightbulb

# Instantiate a Bot instance
bot = lightbulb.BotApp(token="OTEwOTUzNTk4MDg1NjQ0Mjg4.GFSLuC.5Cf3o9qUl0yiods2alTpmtkg7KktbxZXPbumLc",
                       default_enabled_guilds=(),
                       intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print(
        f'Bot Started.\n{event}'
    )


# example
# @bot.command
# # Use the command decorator to convert the function into a command
# @lightbulb.command("ping", "checks the bot is alive")
# # Define the command type(s) that this command implements
# @lightbulb.implements(lightbulb.SlashCommand)
# # Define the command's callback. The callback should take a single argument which will be
# # an instance of a subclass of lightbulb.context.Context when passed in
# async def ping(ctx):
#     # Send a message to the channel the command was used in
#     await ctx.respond("Pong!")

bot.load_extensions_from('./extensions')

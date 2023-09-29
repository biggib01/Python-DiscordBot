import openai
import hikari
import lightbulb

plugin = lightbulb.Plugin('openai')

openai.api_key = "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"

@plugin.command
@lightbulb.option('message', 'message to ask an ai', type=str)
@lightbulb.command('opanai', 'Use open AI')
@lightbulb.implements(lightbulb.SlashCommand)
async def opanai(ctx):

    # query = ctx.options.message
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=query,
    #     temperature=0.3,
    #     max_tokens=2048,
    #     top_p=1,
    #     frequency_penalty=1,
    #     presence_penalty=1,
    #     stop=[" Human:", " AI:"]
    # )
    #
    # text = response['choices'][0]['text']
    # await ctx.respond(" " + text)

    await  ctx.respond("Sorry, we are currently not available for this function")

def load(bot):
    bot.add_plugin(plugin)
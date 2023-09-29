import hikari
import lightbulb
import requests

plugin = lightbulb.Plugin('genAnimePic')


@plugin.command
@lightbulb.option('tagname', 'Tag', str)
@lightbulb.command('generate_anime_pic', 'get sfw anime girl')
@lightbulb.implements(lightbulb.SlashCommand)
async def genpic(ctx):
    try:
        r = requests.get("https://api.waifu.pics/sfw/" + ctx.options.tagname)
        res = r.json()
        em = hikari.Embed()
        em.set_image(res['url'])
        await ctx.respond(em)
    except Exception as e:
        print(e)
        await ctx.respond("Sorry!, I cannot find the picture with this tag! Try `/tag_list` for tag list!")


@plugin.command
@lightbulb.command('tag_list', 'get generate anime pic tag list')
@lightbulb.implements(lightbulb.SlashCommand)
async def taglist(ctx):
    await ctx.respond(">>> ☉ waifu\n☉ neko\n☉ shinobu\n☉ megumin"
                      "\n☉ bully\n☉ cuddle\n☉ cry\n☉ hug\n☉ awoo"
                      "\n☉ kiss\n☉ lick\n☉ pat\n☉ smug\n☉ bonk"
                      "\n☉ yeet\n☉ blush\n☉ smile\n☉ wave\n☉ highfive"
                      "\n☉ handhold\n☉ nom\n☉ bite\n☉ glomp\n☉ slap"
                      "\n☉ kill\n☉ kick\n☉ happy\n☉ wink\n☉ poke\n☉ dance"
                      "\n☉ cringe")


def load(bot):
    bot.add_plugin(plugin)

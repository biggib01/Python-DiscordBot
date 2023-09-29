import hikari
import lightbulb
import testRun

from datetime import datetime

plugin = lightbulb.Plugin('replyOnMessage')

# IN GUILD CHAT #
# record create chat log
@plugin.listener(hikari.GuildMessageCreateEvent)
async def createchatlog(event):

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if event.author == hikari.User:
        return

    username = str(event.author)
    user_message = str(event.content)
    ch = str(event.get_channel())

    print(f'{username} said: "{user_message}" \nin {ch} ch at [{dt_string}]')


# record delete chat log
@plugin.listener(hikari.GuildMessageDeleteEvent)
async def deletechatlog(event):

    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    ch = str(event.get_channel())

    print(f'Chat log in "{ch}" ch get deleted! at [{dt_string}]')


# respond to user
@plugin.listener(hikari.GuildMessageCreateEvent)
async def bothonestreactiontourmention(event) -> None:
    if not event.is_human:
        return

    user_message = str(event.message.content.lower())

    me = testRun.bot.get_me()

    if me.id in event.message.user_mentions_ids and user_message.find("what is your reaction") != -1:
        # need to be reply
        await event.message.respond("https://tenor.com/view/my-honest-reaction-honest-reaction-robert-pattinson-luxury-meme-batman-honest-reaction-gif-27703605")

@plugin.listener(hikari.GuildMessageCreateEvent)
async def sayhi(event) -> None:
    if not event.is_human:
        return
    user_message = event.message.content.lower()

    if user_message == "hello" or user_message == "hi":
        # need to be reply
        await event.message.respond("HI!")


@plugin.listener(hikari.GuildMessageCreateEvent)
async def mutsukireply(event) -> None:
    if not event.is_human:
        return
    user_message = str(event.message.content.lower())

    if user_message.find("mutsuki") != -1:
        # need to be reply
        await event.message.respond("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNIk4Lrztbkqb0nBQEnHZEMOLmdVu1yMuMudOC6NYNZ8rMRxByXylf7QM7HtW0fnGmfTI&usqp=CAU")


@plugin.listener(hikari.GuildMessageCreateEvent)
async def greeting(event) -> None:
    if not event.is_human:
        return
    user_message = event.message.content.lower()

    if user_message == "how are you doing":
        # need to be reply
        await event.message.respond("I'm good! Hope you are too :)")


# IN DM CHAT #
# record bot's DM
@plugin.listener(hikari.DMMessageCreateEvent)
async def recbotsdm(event):
    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    username = event.message.author
    message = event.message.content

    if not event.is_human:
        return

    print(f'Your bot just got new DM fromat {username} : "{message}" \nat[{dt_string}]')

#respond to user in dm
@plugin.listener(hikari.DMMessageCreateEvent)
async def sayhi(event) -> None:
    if not event.is_human:
        return
    user_message = event.message.content.lower()

    if user_message == "hello" or user_message == "hi":
        # need to be reply
        await event.message.respond("HI!")

def load(bot):
    bot.add_plugin(plugin)

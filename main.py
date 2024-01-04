import discord

import utils
import variables
from History.history import *
from api.command_function.system import setLanguage
from conversation import conversationData, Conversation
from string_variables import lang

intents = discord.Intents.all()

from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=intents)

print("Set Language...")
setLanguage()
conversationData.convTree = Conversation()
print("Bot load History...")
load_history()


@client.command(name="Hello")
async def delete(ctx):
    messages = await ctx.channel.userHistory(limit=10)

    for each_message in messages:
        await each_message.delete()


@client.event
async def on_ready():
    print("Bot ready !")
    print(conversationData.__str__())


@client.event
async def on_typing(channel, user, when):
    return


@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044900412551073832)
    await general_channel.send(member.name + " Enter in the pit stop!")
    addUserToHistory(member.id)


is_on = False


@client.event
async def on_message(message):
    global is_on
    if message.author == client.user:
        return

    message.content = message.content.lower()
    # si le message ne provient pas d'un bot
    if not message.author.bot:
        variables.var.messageAuthor = message.author.id
        if message.content.startswith("botbox"):
            variables.var.author_id.append(message.author.id)
            conversationData.convTree.convTree.reset()
            is_on = True
            add_line_to_history(message, response="botbox")
            await message.channel.send(conversationData.convTree.convTree.root.data)
        elif message.content.startswith("help"):
            add_line_to_history(message, response="help")
            await message.channel.send(lang["HELP"])
        elif message.content.startswith("reset") and is_on:
            is_on = False
            # Add to history
            add_line_to_history(message, response="stop")
            await message.channel.send(lang["END_RESPONSE"])
        elif is_on and utils.listContains(variables.var.author_id, message.author.id):
            if "-limit" in message.content:
                message.content, tmp = utils.getValueOfParameter(message.content, "-limit")
                variables.var.call_limit = "?limit=" + tmp
                print("SYSTEM: call_limit = " + variables.var.call_limit)
            if "-lang" in message.content:
                message.content, variables.var.language = utils.getValueOfParameter(message.content, "-lang")
                print("SYSTEM: language = " + variables.var.language)
            if "-year" in message.content:
                message.content, tmp = utils.getValueOfParameter(message.content, "-year")
                variables.var.year = tmp + "/"
                print("SYSTEM: year = " + variables.var.year)
            if "-constructor" in message.content:
                message.content, tmp = utils.getValueOfParameter(message.content, "-constructor")
                variables.var.constructor = "constructors/" + tmp + "/"
                print("SYSTEM: constructor = " + variables.var.constructor)
            if "-circuit" in message.content:
                message.content, tmp = utils.getValueOfParameter(message.content, "-circuit")
                variables.var.circuit = "circuits/" + tmp + "/"
                print("SYSTEM: circuit = " + variables.var.circuit)
            if "-driver" in message.content:
                message.content, tmp = utils.getValueOfParameter(message.content, "-driver")
                variables.var.driver = tmp
                print("SYSTEM: driver = " + variables.var.driver)
            if "-about" in message.content:
                message.content, tmp = utils.getValueOfParameter(message.content, "-about")
                variables.var.about = tmp
                print("SYSTEM: about = " + variables.var.about)

            bot_message = conversationData.convTree.convTree.send_answer(str(message.content))

            # Add to history
            add_line_to_history(message, response=bot_message)

            # print("=> '" + bot_message + "'")

            # si les 4 derniers caractere sont "#end"
            if bot_message[-4:] == "#end":
                bot_message = bot_message[:-4]
                if variables.var.auto_restart:
                    # await message.channel.send(conversation.root.data)
                    print("SYSTEM: end conversation and dont restart")
                else:
                    is_on = False
                    print("SYSTEM: end conversation")

            # gestion des messages trop longs
            if bot_message is not None and len(bot_message) < 2000:
                await message.channel.send(bot_message)
            elif bot_message is not None and len(bot_message) >= 2000:
                for i in range(0, len(bot_message), 2000):
                    await message.channel.send(bot_message[i:i + 2000])

    await client.process_commands(message)


client.run(utils.readToken())

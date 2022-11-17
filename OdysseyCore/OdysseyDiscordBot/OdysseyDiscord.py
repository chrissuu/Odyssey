import discord
import os.path

from os import path

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
discordTOKEN = "MTAxMDY0ODk4NzA1OTA5Nzc4MQ.Gq28f0.7eXr6eLHkXWskwEp2_iV32X9d1xchxnTrlJNQc"

verifiedUserDict = {"khris": "556572931036282898"}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('^**passhelp'):
        await message.channel.send(
            "getpasslist - return available password queries\npasslistdraft (str name) - makes new password query "
            "draft with name 'name'\npass")

    if message.content.startswith('^**getpasslist'):
        await message.channel.send("hi")

    if message.content.startswith('^**passlistdraft'):
        passEditList = message.content.split()

        try:
            f = open("passlistDirectory/" + passEditList[1] + ".txt", "x")
        except:
            await message.channel.send("File with same name already exists.")
        else:
            # passname = website/app domain
            f.write("***" + passEditList[1] + "^")
            f.close()

    # a - append, w - write (overwrites existing), x - create new file, returns error if already exists, r - read file

    if message.content.startswith('^**passeditdomain'):
        passEditList = message.content.split()

        passEditName = passEditList[1]
        passEditDomain = passEditList[2]

        fileExists = path.exists("passlistDirectory/" + passEditName + ".txt")

        parsedQueryList = parseIncompleteQuery("passlistDirectory/" + passEditName + ".txt")

        if len(parsedQueryList['***']) > 0:
            await message.channel.send("File already has domain name.")
        else:
            if fileExists:

                if len(parsedQueryList['***']) > 0:

                    await message.channel.send("Query already a domain.")

                else:

                    f = open("passlistDirectory/" + passEditName + ".txt", "a")
                    f.write("***" + passEditDomain + "^")
                    f.close()

            else:
                await message.channel.send("File with that name does not exist.")

    # passedituser (str fileName) (str username) - adds username to password query
    if message.content.startswith('^**passedituser'):
        passEditList = message.content.split()

        passEditName = passEditList[1]
        passEditUser = passEditList[2]

        fileExists = path.exists("passlistDirectory/" + passEditName + ".txt")

        if fileExists:
            parsedQueryList = parseIncompleteQuery("passlistDirectory/" + passEditName + ".txt")

            missingCount = 0

            mes = "Query is missing: "

            if len(parsedQueryList['***']) == 0:

                missingCount += 1
                mes += "[domain]"

            if missingCount > 0:

                await message.channel.send(mes)

            else:
                if len(parsedQueryList['@@@']) > 0:

                    await message.channel.send("Query already a username.")

                else:

                    f = open("passlistDirectory/" + passEditName + ".txt", "a")
                    f.write("@@@" + passEditUser + "^")
                    f.close()

        else:

            await message.channel.send("File with that name does not exist.")

    # passeditpass (str fileName) (str password) - adds password to password query
    if message.content.startswith('^**passeditpass'):
        passEditList = message.content.split()

        passEditName = passEditList[1]
        passEditPass = passEditList[2]

        fileExists = path.exists("passlistDirectory/" + passEditName + ".txt")

        if fileExists:
            parsedQueryList = parseIncompleteQuery("passlistDirectory/" + passEditName + ".txt")

            missingCount = 0

            mes = "Query is missing: "

            if len(parsedQueryList['***']) == 0:

                missingCount += 1
                mes += "[domain]"

            if len(parsedQueryList['@@@']) == 0:

                missingCount += 1
                mes += "[username]"

            if missingCount > 0:

                await message.channel.send(mes)

            else:
                if len(parsedQueryList['@@*']) > 0:

                    await message.channel.send("Query already a password.")

                else:

                    f = open("passlistDirectory/" + passEditName + ".txt", "a")
                    f.write("@@*" + passEditPass + "^")
                    f.close()

        else:

            await message.channel.send("File with that name does not exist.")

    # passeditdes (str fileName) (str description) - adds description to password query
    if message.content.startswith('^**passeditdes'):
        passEditList = message.content.split()

        passEditName = passEditList[1]

        passEditDescription = ""
        for x in range(2, len(passEditList)):
            passEditDescription += passEditList[x] + " "
        passEditDescription = passEditDescription[0:len(passEditDescription) - 1]

        fileExists = path.exists("passlistDirectory/" + passEditName + ".txt")

        if fileExists:
            parsedQueryList = parseIncompleteQuery("passlistDirectory/" + passEditName + ".txt")

            missingCount = 0

            mes = "Query is missing: "

            if len(parsedQueryList['***']) == 0:

                missingCount += 1
                mes += "[domain]"

            if len(parsedQueryList['@@@']) == 0:

                missingCount += 1
                mes += "[username]"

            if len(parsedQueryList['@@*']) == 0:

                missingCount += 1
                mes += "[password]"

            if missingCount > 0:

                await message.channel.send(mes)

            else:

                if len(parsedQueryList['@**']) > 0:

                    await message.channel.send("Query already a description.")

                else:

                    f = open("passlistDirectory/" + passEditName + ".txt", "a")
                    f.write("@**" + passEditDescription + "^")
                    f.close()

        else:

            await message.channel.send("File with that name does not exist.")

    if message.content.startswith('^**passdel'):
        passName = message.content.split()[1]

        fileExists = path.exists("passlistDirectory/" + passName + ".txt")

        if fileExists:
            os.remove("passlistDirectory/" + passName + ".txt")
        else:
            await message.channel.send("File with that name does not exist.")

    if message.content.startswith('^**parseQuery'):
        fileName = message.content.split()[1]

        await message.channel.send(parseQuery("passlistDirectory/" + fileName + ".txt"))

    if message.content.startswith('^**queryList'):
        queryList = os.listdir("passlistDirectory/")

        await message.channel.send(str(queryList))


def parseIncompleteQuery(fileName):
    dataTypes = {"***": "", "@@@": "", "@@*": "", "@**": ""}
    file = open(fileName, "r")

    query = str(file.read())

    dataList = query.split("^")

    for D in dataList:
        dataType = D[0:3]
        data = D[3:]

        dataTypes[dataType] = data

    return dataTypes


def parseQuery(fileName):

    file = open(fileName, "r")

    query = file.read()

    dataList = query.split("^")

    strDomain = dataList[0]
    strUsername = dataList[1]
    strPassword = dataList[2]

    strDescription = ""
    if len(query) > len(strDomain + strUsername + strPassword) + 3:
        strDescription += dataList[3]

    domain = strDomain[3:]
    username = strUsername[3:]
    password = strPassword[3:]

    description = ""
    if len(strDescription) > 0:
        description += strDescription[3:]

    returnMes = "Domain: " + domain + "\n" + "Username: " + username + "\n" + "Password: " + password + "\n" + "Description: " + description
    return returnMes


client.run(discordTOKEN)











































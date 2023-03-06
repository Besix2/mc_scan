import socket
import pymongo
import lightbulb
import hikari


client = pymongo.MongoClient("mongo-container:27017")
db = client["treffer"]
collection = db["ips"]
if client.server_info():
    print("Connected to MongoDB successfully!")
else:
    print("Could not connect to MongoDB.")
v_list = ["1.19.3", "1.19.2", "1.19.1", "1.19", "1.18.2", "1.18.1", "1.18", "1.17.1", "1.17", "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.16", "1.15.2", "1.15.1", "1.15", "1.14.4", "1.14.3", "1.14.2", "1.14.1", "1.14", "1.13.2", "1.13.1", "1.13", "1.12.2", "1.12.1", "1.12", "1.11.2", "1.11.1", "1.11", "1.10.2", "1.10.1", "1.10", "1.9.4", "1.9.3", "1.9.2", "1.9.1", "1.9", "1.8.9"]

with open("config.txt","r") as config:
    lines = config.readlines()
    l3 = lines[2].strip()
print(l3)

bot = lightbulb.BotApp(token=f"{l3}")
rounds = 0
last_version = ""

@bot.command()
@lightbulb.option("version", "Version: 1.19.3, 1.19.2 ... or all",type=str)
@lightbulb.command("entrys", "returns number of servers")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    version = ctx.options.version
    if version not in v_list and version != "all":
        await ctx.respond("Wrong input for version number")
    else:
        if version[0] == "1":
            print(version)
            results = collection.find({"status.version.name": version})
            ip_list = [i["ip"] for i in results]
            await ctx.respond(f"There are {len(ip_list)} Server with the version {version}")
        else:
            await ctx.respond(f"There are currently {collection.count_documents({})} Server")

@bot.command()
@lightbulb.option("results", "the number of results to show( max. 15)",type=int)
@lightbulb.option("version", "The version number(e.g. 1.19.3)", type=str)
@lightbulb.command("server", "find server Ip's")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    global rounds
    global last_version
    version = ctx.options.version
    result_number = ctx.options.results
    if version not in v_list:
        await ctx.respond("Wrong input for version number")
    elif result_number > 15 or result_number < 0:
        await ctx.respond("Wrong input for result number")
    else:
        results = collection.find({"status.version.name": version})
        ip_list = [i["ip"] for i in results]
        c_value = len(ip_list) - rounds

        if len(ip_list) < result_number:
            await ctx.respond("Currently there are not that much results for version {}. (only {}).\nShowing what we got so far.\nIP addresses: \n{}".format(version, len(ip_list), '\n'.join(ip_list)))
            last_version = version

        elif c_value == 0:
            await ctx.respond("Outputted all Ip adresses for that version. Resetting...")
            rounds = 0

        else:
            if last_version == version:
                await ctx.respond("Version: {}\nIP addresses: \n{}".format(version, '\n'.join(ip_list[rounds:rounds + result_number])))
            else:
                await ctx.respond("Version: {}\nIP addresses: \n{}".format(version, '\n'.join(ip_list[:result_number])))
            rounds = rounds + result_number
            last_version = version


bot.run()

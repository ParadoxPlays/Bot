import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix="!", case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    os.system("clear")
    print(f"{client.user} is online!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!, Bot Latency: {round(client.latency * 1000)}ms.")

client.run("TOKEN")

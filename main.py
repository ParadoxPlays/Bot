#main.py
import disnake
from disnake.ext import commands
import random

intents = disnake.Intents.all()

#Ensure you are not using a prefix that another bot has, if so it will be buggy.
PREFIXES = ["!", "?", "-", ".", ","]

client = commands.Bot(command_prefix=PREFIXES, intents=intents, case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    os.system("clear")
    print(f"{client.user} is online!")

@client.command()
async def ping(ctx):
    await ctx.reply(f"Pong!, Bot Latency: {round(client.latency * 1000)}ms.")

@client.command(aliases=["8b", "8ball", "eb"])
async def eightball(ctx, *, question):
    responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    await ctx.reply(f":8ball: Your Question: {question}\n:8ball: Answer: {random.choice(responses)}")

@client.command()
async def status(ctx, *, activity):
    await client.change_presence(activity=disnake.Game(name=activity))
    await ctx.reply(f"Status changed to {activity}.")

@client.command()
async def add(ctx, left: float, right: float):
    await ctx.reply(f"Answer: {str(left + right)}")

@client.command()
async def subtract(ctx, left: float, right: float):
    await ctx.reply(f"Answer: {str(left - right)}")

@client.command()
async def multiply(ctx, left: float, right: float):
    await ctx.reply(f"Answer: {str(left * right)}")

@client.command()
async def divide(ctx, left: float, right: float):
    await ctx.reply(f"Answer: {str(left / right)}")

client.run("TOKEN")

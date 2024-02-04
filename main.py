#main.py
import disnake
from disnake.ext import commands
import random
from disnake import Interaction
from disnake import Intents
from disnake import Select, View

intents = disnake.Intents.all()

#Ensure you are not using a prefix that another bot has, if so it will be buggy.
PREFIXES = ["!", "?"]

client = commands.Bot(command_prefix=PREFIXES, intents=intents, case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    os.system("clear")
    print(f"{client.user} is online!")
    client.add_view(Verify())

@client.slash_command()
async def verify(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message("Verification View Sent.", ephemeral=True)
    embed = disnake.Embed(title="Verify", description="Click the button below to verify and gain access to the rest of the discord.", color=0x0000AA)
    await inter.channel.send(embed=embed, view=Verify())

class Verify(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @disnake.ui.button(label="Verify", style=disnake.ButtonStyle.grey, custom_id="verify:grey")
    async def verify(self, button: disnake.ui.Button, interaction: disnake.Interaction):
    #Replace Member with whatever role you want the user to receive upon verifying.
        role = disnake.utils.get(interaction.guild.roles, name="Member")
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"Thank you for verifying {user.mention}.", ephemeral=True)

@client.slash_command()
async def ping(inter: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(title="Pong!", description=f"Client Latency: {round(client.latency * 1000)}ms")
    await inter.response.send_message(embed=embed)

@client.slash_command(aliases=["8b", "8ball", "eb"])
async def eightball(inter: disnake.ApplicationCommandInteraction, *, question):
    responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    await inter.response.send_message(f":8ball: Your Question: {question}\n:8ball: Answer: {random.choice(responses)}")

@client.slash_command()
async def status(inter: disnake.ApplicationCommandInteraction, *, activity):
    await client.change_presence(activity=disnake.Game(name=activity))
    await inter.response.send_message(f"Status changed to {activity}.")

@client.slash_command()
async def add(inter: disnake.ApplicationCommandInteraction, left: float, right: float):
    await inter.response.send_message(f"Answer: {str(left + right)}")

@client.slash_command()
async def subtract(inter: disnake.ApplicationCommandInteraction, left: float, right: float):
    await inter.response.send_message(f"Answer: {str(left - right)}")

@client.slash_command()
async def multiply(inter: disnake.ApplicationCommandInteraction, left: float, right: float):
    await inter.response.send_message(f"Answer: {str(left * right)}")

@client.slash_command()
async def divide(inter: disnake.ApplicationCommandInteraction, left: float, right: float):
    await inter.response.send_message(f"Answer: {str(left / right)}")

client.run("TOKEN")

import discord
from discord.ext import commands
import os
import requests as r
PREFIX = "!"
BANNED_WORDS = [
  "pizza hawaii","scriptie" 
]

intent = discord.Intents.default()
intent.members = True

client = commands.Bot(intent=intent, command_prefix=PREFIX)

@client.command()
async def koffie(context):
  req = r.get("https://coffee.alexflipnote.dev/random.json")
  res = req.json()
  await context.message.reply(res["file"])

@client.command()
async def kat(context):
  req = r.get("https://api.thecatapi.com/v1/images/search")
  res = req.json()
  await context.message.reply(res[0]["url"])

@client.command()
async def hoi(context):
	await context.message.reply("Hallo!")

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")

@client.event
async def on_member_join(member):
  print("member joined")
  guild = member.guild
  if guild.system_channel is not None:
    res =f"Welkom {member.mention} in de {guild.name} server!"
    await guild.system_channel.sent(res)

@client.event
async def on_message(message):
  if message.author.id == client.user.id:
    return
  for word in BANNED_WORDS:
    if word in message.content.lower():
      await message.delete()
      await message.channel.send(f"{message.author.mention} je bericht is verwijderd,omdat het een verbode woord bevat")
  await client.process_commands(message)


client.run(os.getenv("TOKEN"))
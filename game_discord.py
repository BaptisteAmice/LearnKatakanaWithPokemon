import os
import asyncio
import discord
from discord import app_commands
import japanese as japanese
import pokemon_api as pokemon_api
import sqlite_utility as sql_utility
from prettytable import PrettyTable as pt
from dotenv import find_dotenv, load_dotenv


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_TOKEN = os.getenv("API_TOKEN")


intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
intents.messages = True
intents.reactions = True
intents.guilds = True
intents.emojis = True
intents.guild_messages = True
intents.guild_reactions = True
intents.guilds = True
intents.guild_typing = True
intents.guilds = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#command to guess the name of a pokemon in another language
@tree.command(name = "pt", description = "Guess the translation of a random pokemon name from japanese") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def gess_pokemon_name_translation(ctx, language: str):

  player = ctx.user
  sql_utility.add_player(player.id, player.name+"#"+player.discriminator)

  channel = ctx.channel

  pokemon_id= pokemon_api.get_random_pokemon_id()
  names = pokemon_api.get_pokemon_names(pokemon_id, ['ja', language])
  if(names.__len__() < 2):
    #some pokemon aren't translated in all languages, but this will be fixed in the future, so we can just try again to diminish the chance of this happening
    pokemon_id= pokemon_api.get_random_pokemon_id()
    names = pokemon_api.get_pokemon_names(pokemon_id, ['ja', language])
    if(names.__len__() < 2):
      await channel.send("Error: pokemon not found")
    return
  await channel.send("What is the name of this pokemon in " + language + "?\n"+names[0])
  try:

    #get value
    answer = await client.wait_for('message', check=lambda message: channel == message.channel, timeout=60.0)
  except asyncio.TimeoutError:
    await channel.send('Sorry, you took too long')
  else:
    if answer.content.lower() == names[1].lower():
      await channel.send("Correct!")
      sql_utility.increment_player_sc_romaji(player.id, 1)
    else:
      await channel.send("Wrong! The correct answer is " + names[1])


#command to guess the name of a pokemon in romaji
@tree.command(name = "pr", description = "Guess the romaji of a random pokemon name") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def gess_pokemon_name_in_romanji(ctx):

  player = ctx.user
  sql_utility.add_player(player.id, player.name+"#"+player.discriminator)
  
  channel = ctx.channel

  pokemon_id= pokemon_api.get_random_pokemon_id()
  name = pokemon_api.get_pokemon_names(pokemon_id, ['ja'])[0]
  await channel.send("What is this pokemon's name in romaji?")
  await channel.send(name)
  try:
    #get value
    answer = await client.wait_for('message', check=lambda message: channel == message.channel, timeout=60.0)

  except asyncio.TimeoutError:
    await channel.send('Sorry, you took too long')
  else:

    if answer.content.lower() == japanese.japanese_to_romanji(name).lower():
      await channel.send("Correct!")
      sql_utility.increment_player_sc_romaji(player.id, 1)
    else:
      await channel.send("Wrong! The correct answer is " + japanese.japanese_to_romanji(name))
  

#command to print the leaderboard
@tree.command(name = "lb", description = "Print the leaderboard") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def print_leaderboard(ctx):
  channel = ctx.channel
  ranking = sql_utility.get_leaderboard()
  table = pt()
  table.field_names = ["Rank", "Name", "Translation Points", "Romaji Points", "Total Points"]
  for i in range(ranking.__len__()):
    table.add_row([i+1, ranking[i][0], ranking[i][1], ranking[i][2], ranking[i][3]])
  await channel.send("```" + table.get_string() + "```")

@client.event
async def on_ready():
    await tree.sync() #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
    print("Ready!")

client.run(API_TOKEN)

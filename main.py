import discord
import os
import random
from Chat import Add_Response
from Chat import Get_Response
from Chat import CanAddResponses
from Chat import CanRespond
from discord.ext import commands


bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='kpop'))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
      
  WholeMessage = message.content

  if not CanRespond():
    return 
  SendMessage = Get_Response(WholeMessage)
  if SendMessage != "":
    await message.channel.send(SendMessage)
  await bot.process_commands(message)


@bot.command(
  help = ""
)
async def addresponse(message , *args):
  isResponse = True
  WholeMessage = ""
  Response = ""
  for message in args:
    if message == "$x":
      isResponse = not isResponse
    else:
      if not isResponse:
        WholeMessage += message + " "
      else:
        Response += message + " "

  Add_Response(WholeMessage,Response)

@bot.command(
  help = """$WipeHistory <User> <filter> <Limit>
  <Limit> is the total number of messages to iterate (not just <User>)
  """
)
async def WipeHistory(client , user , filter , number):
  await client.message.delete()
  msg = []
  async for message in client.message.channel.history(limit=int(number)):
    if filter in message.content:
      authorid = "<@!"+ str(message.author.id) + ">"
      if authorid == user:
        msg.append(message)
  
  await client.message.channel.delete_messages(msg)
bot.run(os.getenv('TOKEN')) 

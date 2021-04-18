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


@bot.command()
async def addresponse(message , *args):
  Response 
  await message.channel.send("testing :)") 

bot.run(os.getenv('TOKEN')) 

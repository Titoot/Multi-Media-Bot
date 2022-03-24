import os
import discord
import tiktok
import facebook
import pastebin
import re
from keep_alive import keep_alive
#os.system('pip install yt-dlp')

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()
mainRegex = r'\s*(.*)'

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

      
    if message.content == '!list':
      supported = ['tiktok','facebook','pastebin']
      lister = 'supported:\n'
      for i in supported:      
        lister += i + '\n'        
      await message.channel.send(lister)
    #GET URLS

      
    commD = '!d'
    
    if commD in message.content:
      mess = re.match(commD+mainRegex, message.content)[1]
      print(mess)
      if mess:
        if 'tiktok.com' in mess :
          
            if tiktok.VerifyLink(mess):
                await message.channel.send('TikTok Link Identefied!')           
            await message.channel.send(f"||{tiktok.get_url(mess)}||")
          
    
        elif 'facebook.com' in mess:
          
          await message.channel.send(f"||{facebook.download(mess)}||")
          #await message.channel.send('facebook?')

        elif 'pastebin.com' in mess:
          paste, type = pastebin.get_paste(mess)
          for i in paste:
            i = i.replace('    ','\n')
            await message.channel.send(f'```{type}\n{i}```')
        else:
          await message.channel.send('Error: Unsupported URL, see !list')
      else:
        await message.channel.send('Error: Unsupported URL, see !list')
        
        
keep_alive()
client.run(TOKEN)

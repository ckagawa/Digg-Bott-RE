import discord
import os
import re
import random
import diggdict
##import youtube_dl

##cogs = [music.music]

##client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

##for i in cogs:setup(client)
#Voice client
vc = None
#Client object
me = discord.Client()
#command dictionary
lib = diggdict.setup(me)

@me.event
async def on_ready():
  print('We have logged in as {0.user}'.format(me))

@me.event
async def on_message(message):
  if message.author == me.user:
    return
  #regex, any number of whitespace chars,1 or more non-whitespace chars,1 or more whitespace chars, any number of non-whitespace chars
  t1 = re.compile('\s*\S+\s*')
  #force case to lower, other ways to do this but easy lazy way to make name short
  inp = t1.findall(message.content.lower()).group()
##join bot
## if message.content.startswith('digg') or message.content.startswith('Digg'):
##await message.channel.send('SMA!')
  if lib.contains(inp[0]):
    #tuple with method,args
    comm = lib[inp[0]]
    if len(inp)>1:
      comm[0](me.context,comm[1],inp[1]);
    else:
      comm[0](me.context,comm[1],None);
##    voice_channel = message.author.voice.channel
##   if voice_channel:
##     if client.voice_clients:
##       if voice_channel != client.voice_clients:
##         await client.voice_clients[0].move_to(voice_channel)
##       else:
##         pass
##     else:
##        await voice_channel.connect()
##   else:
##    await message.channel.send('SMA!')

##kick bot
##  if message.content.startswith('Kick') or message.content.startswith('kick'):
##  if client.voice_clients:
##      await client.voice_clients[0].disconnect()

##  if message.content.startswith('digg') or message.content.startswith('Digg'):
##    await message.channel.send('SMA!')

##  if message.content.startswith('Game') or message.content.startswith('game'):
##    await message.channel.send('You guys are smol.')

  ##Youtube function
##  if message.content.startswith('play') or message.content.startswith('Play'):
      
##        if client.voice_clients:
##          client.voice_clients[0].stop()
##          FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
##          vc = client.voice_clients[0]
##          url = message.content.split(" ")[1]
          ##ydl_options = {'format':'bestaudio'}
          ##with youtube_dl.YoutubeDL(ydl_options) as ydl:
##            info = ydl.extract_info(url, download=False)
            ##url2 = info['formats'][0]['url']
            ##import pdb; pdb.set_trace()
            ##vc.play(discord.FFmpegPCMAudio.from_probe(#executable='Digg-Bott/runner/   /ffmpeg.exe', source=url2))
            ##ource = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            ##vc.play(source)

      

##  if message.content.startswith('smol') or message.content.startswith('sma'):
##    probability = random.randint(1,4)
##    if probability == 1 or probability == 2:
      ##filepath = str(random.randint(1,6)) + ('.JPG')
      ##with open(filepath, 'rb') as f:
        ##picture = discord.File(f)
        ##await message.channel.send(file=picture)
  
##  if message.content.startswith('stonks'):
    ##filepath = 'stonks.JPG'
    ##with open(filepath, 'rb') as f:
      ##picture = discord.File(f)
      ##await message.channel.send(file=picture)
  
  ##if message.content.startswith('sfw'):
    ##filepath = 'sfwsasuke.jpg'
    ##with open(filepath, 'rb') as f:
      ##picture = discord.File(f)
      ##await message.channel.send(file=picture)
    ##with open(filepath, 'rb') as f:
      ##picture = discord.File(f)
      ##await message.channel.send(file=picture)
    ##with open(filepath, 'rb') as f:
      ##picture = discord.File(f)
      ##await message.channel.send(file=picture)

  ##if message.content.startswith('Believe') or message.content.startswith('believe'):
    ##filepath = 'believe.jpg'
    ##with open(filepath, 'rb') as f:
      ##picture = discord.File(f)
      ##await message.channel.send(file=picture)

  ##if message.content.startswith('Blockchain') or message.content.startswith('blockchain'):
    ##filepath = 'blockchain.gif'
    ##with open(filepath, 'rb') as f:
      ##picture = discord.File(f)
      ##await message.channel.send(file=picture)
  
  ##watch together
  ##if message.content.startswith('watch2gether') or message.content.startswith('Watch2gether'):
    ##await message.channel.send('https://w2g.tv/ndqegp3ip0i2o8kfa7')
  
  ##coin flip
  ##if message.content.startswith('coinflip') or message.content.startswith('Coinflip'):
    ##results = random.randint(1,2)
    ##if results == 1:
      ##filepath = 'heads.png'
      ##with open(filepath, 'rb') as f:
        ##picture = discord.File(f)
        ##await message.channel.send(file=picture)
    ##else:
      ##filepath = 'tails.png'
      ##with open(filepath, 'rb') as f:
        ##picture = discord.File(f)
        ##await message.channel.send(file=picture)
  
  ##if message.content.startswith('smile') or message.content.startswith('hero'):
    ##filepath = 'harsh.png'
    ##with open(filepath, 'rb') as f:
      ##picture = discord.File(f)
      ##await message.channel.send(file=picture)


##my_secret = os.environ['TOKEN']

##me.run(my_secret)



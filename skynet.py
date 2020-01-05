import discord
import time

#client = discord.Client() # when not using prefixes in bot


# for jokes
# ------start-----


import numpy as np
import pandas as pd

z = pd.read_csv('jokes.csv')
k = z.iloc[:, 1:2]
y = np.random.randint(0, len(np.array(k)))
vc = ""
# -----end-----

# security------------------
f = open("token.txt", "r")
t = f.read()
f.close()
#---------------------------


# Commands and Prefixes
#------------------------------

from discord.ext import commands

client = commands.Bot(command_prefix = '$')

#------------------------------


@client.event
async def on_ready():
    # await send("swagat ni karoge hamara!!")
    print("UP AND RUNNING")

# Commands
#------- starts -----------
stop = False # **

@client.command()
async def greet(ctx):
    await ctx.send("hello")
    
@client.command()
async def cmc(ctx):
    await ctx.send("cmc "+ctx.author.mention)

@client.command()
async def jokes(ctx):
    y = np.random.randint(0,len(np.array(k)))
    await ctx.send(np.array(k)[y][0])

@client.command()
async def spam(ctx, *message):
    global stop
    spam = message[:]
    print(spam)        
    size = spam[0]
    tim = spam[1]
    mess = " ".join(spam[2:])
    print (size,tim,mess)
    for x in range(0,int(size)):            
        if stop:
            print("done")
            stop = False
            await ctx.send("Ok Boss spamming is on halt!!")
            break
        else:
            time.sleep(float(tim))
            await ctx.send(mess)
            
@client.command()
async def stop(ctx):
    global stop
    stop = True
"""
@client.command()
async def nikal_lavde(ctx):
    if ts:
        await ctx.invoke(client.get_command("discon")) #lmao discord.py server saved my ass
    await ctx.send("hasta-la-vista baby!!:hand_splayed:")
    exit()
"""
#----------------------- VC commands --------------------------
from gtts import gTTS
import youtube_dl
import os
ts = False
moany = []
for fi in os.listdir('./NSFW/'):
    moany.append(fi)
print(moany)

@client.command()
async def ping(ctx):
    ping = client.latency
    ping = round(ping*1000)
    await ctx.send("ping is "+str(ping)+"ms")

@client.command()
async def connect(ctx):
    global pl
    global vc
    global ts
    ts = True
    #pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source="sup.mp3")
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    await ctx.send("I am here, I AM HEERREEEEEEEE!! AT "+str(channel))
    #vc.play(pl)
    print(channel, vc)

@client.command()
async def discon(ctx):
    global ts
    ts=False
    print(client.voice_clients)
    if len(client.voice_clients)==0:
        await ctx.send("I am not connected to any VC, retarded "+ctx.author.mention+" !!")
    for x in client.voice_clients:
        if len(client.voice_clients)!=0:
            await ctx.send("**SILENT** hojata hu warna mein hi **VIOLENT** hojaunga")
            await x.disconnect()
            

@client.command()
async def play(ctx):    
    global pl
    global vc
    pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source="JOJO.mp3")
    vc.play(pl)
    
@client.command()
async def tts(ctx,*mes):
    global pl
    global vc
    #print("haha")
    print(mes)
    print(" ".join(mes))
    speech = gTTS(" ".join(mes), 'en')
    var = "ply"
    #print("doneo")
    speech.save(var+".mp3")
    print("ok")
    pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source="ply.mp3")
    vc.play(pl)

@client.command()
async def pause(ctx):
    global vc
    vc.pause()

@client.command()
async def ruk(ctx):
    global vc
    vc.stop()

@client.command()
async def resume(ctx):
    global vc
    vc.resume()
players = {}
@client.command()
async def yt(ctx, url):
    global vc
    global pl
    song = False
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
             'preferredquality': '192',
            }
        ],
        'outtmpl':'./songs/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url,download=False)
    #print("hello")
    for file in os.listdir('./songs/'):
        if file.endswith(".webm"):
            os.rename(file, "song.mp3")
    x = info_dict['title']
    print(x[:-1])
    for file in os.listdir('./songs/'):
        print(file)
        if file.startswith(x[:-1]):
            song = True
            break
    if song:
            pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source="./songs/"+file)
            vc.play(pl)
    else:
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url,download=True)
        for file in os.listdir('./songs/'):
            if file.startswith(x[:-1]):
                break
        print(file)
        pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source="./songs/"+file)
        vc.play(pl)    

@client.command()
async def moan(ctx):
    global vc
    global pl
    yi = np.random.randint(0,len(moany))
    print("jaj")
    sor = "./NSFW/"+moany[yi]
    pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source=sor)
    print("lal")
    vc.play(pl)

@client.command()
async def meme(ctx,*me):
    global vc
    global pl
    pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source="./meme/"+me[0]+".mp3")
    vc.play(pl)

#------------------------------ VC end ---------------------------

#------- end --------------



"""
@client.event
async def on_message(message):
    global k
    global stop # **
    if message.author == client.user:
        print("\n yeah same!!" + " " + str(stop))
    if message.content.startswith("stop"):
        stop = True
    if message.content.startswith('$heyo'):
        x = message.content.startswith('$heyo')
        print(x)
        await message.channel.send('\n jhalta hai!!')
    if message.content.startswith('god kon hai'):
        await message.channel.send('senpai aap ho SAM THE GOD!!')
    if message.content.startswith('retard bot'):
        await message.channel.send('go fuck yourself!! :rage:  :middle_finger: :imp: ')
    if message.content.startswith('wishes'):
        await message.channel.send('happy diwali to you all retards!!:middle_finger: :spy: ')
#-----------------------------------------------------------
    if message.content.startswith('jokes') or message.content.startswith('Jokes'):
        y = np.random.randint(0,len(np.array(k)))
        await message.channel.send(np.array(k)[y][0])
#-----------------------------------------------------------
        
    if message.content.startswith("$cmc"):
        await message.channel.send("cmc "+message.author.mention)

# spamming # **
#---------- start ------------
    if message.content.startswith('$spam'):
        spam = message.content.lower().split(" ")
        print(spam)
        size = spam[1]
        tim = spam[2]
        mess = " ".join(spam[3:])
        for x in range(0,int(size)):            
            if stop:
                print("done")
                await message.channel.send("Ok Boss spamming is on halt!!")
                stop = False
                break
            else:
                time.sleep(int(tim))
                await message.channel.send(mess)
# ---------- end -------------

    if message.content.startswith('rukja client'):
        await message.channel.send("hasta-la-vista baby!!:hand_splayed:")
        exit(0)
    #if message.content.startswith("$greet"):
        #await client.process_commands(message)
"""
client.run(t)

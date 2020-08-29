import discord
import time
import cipher
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
t = cipher.dec(t) # <---- uncomment this code 


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

#____________________ Tic Tac Toe ________________________

played = []
xColumn = []
xRow= []
oColumn= []
oRow= []

theBoard = {"t-l":".","t-m":".","t-r":".",
            "m-l":".","m-m":".","m-r":".",
            "b-l":".","b-m":".","b-r":".",}

theCheck = {"t-l":[1,1],"t-m":[1,2],"t-r":[1,3],
            "m-l":[2,1],"m-m":[2,2],"m-r":[2,3],
            "b-l":[3,1],"b-m":[3,2],"b-r":[3,3],}
play = True
Turn = "X"

def ticBoard (board):
    """print(board["t-l"]+"|"+board["t-m"]+"|"+board["t-r"])
    print("-+-+-")
    print(board["m-l"]+"|"+board["m-m"]+"|"+board["m-r"])
    print("-+-+-")
    print(board["b-l"]+"|"+board["b-m"]+"|"+board["b-r"])"""
    
    return(board["t-l"]+"|"+board["t-m"]+"|"+board["t-r"]+"\n"
          +"---+--+---"+"\n"+board["m-l"]+"|"+board["m-m"]+"|"
          +board["m-r"]+"\n"+"---+--+---"+"\n"+board["b-l"]+"|"
          +board["b-m"]+"|"+board["b-r"])

@client.command()
async def tac(ctx):
    global play,xColumn,xRow,oColumn,oRow,theBoard,Turn,played,theCheck
    if play:
        played = []
        xColumn = []
        xRow= []
        oColumn= []
        oRow= []

        theBoard = {"t-l":".\t","t-m":"\t","t-r":" ",
                    "m-l":".\t","m-m":"\t","m-r":" ",
                    "b-l":".\t","b-m":"\t","b-r":" ",}
        Turn = "X"
        await ctx.send("Welcome to Tic-Tac-Toe")
        await ctx.send(ticBoard(theBoard))
        await ctx.send("Player '{}'. Move where?".format(Turn))
        play = False
    else:
        await ctx.send("Game is ongoing can't start. Use $resettic to reset")

@client.command()
async def toe(ctx,*mes):
    move = mes[0]
    global play,xColumn,xRow,oColumn,oRow,theBoard,Turn,played,theCheck
    if not play:
        if (move not in theBoard.keys()):
            await ctx.send("Please type it correctly!!")
        else:
            if move in played:
                await ctx.send("Already occupied!!")
            else:
                theBoard[move] = Turn
                played.append(move)
                if Turn == "X":
                    xColumn.append(theCheck[move][1])
                    xRow.append(theCheck[move][0])
                    if (                                           
                        xColumn.count(theCheck[move][1]) == 3 
                        or xRow.count(theCheck[move][0]) == 3 
                        or {1,2,3}==set(set(xColumn).intersection(xRow)).intersection([1,2,3])
                    ):
                        #used set and intersection
                        await ctx.send("Player X Wins!!")
                        play = True
                    Turn = "O"
                else:
                    oColumn.append(theCheck[move][1])
                    oRow.append(theCheck[move][0])
                    if (
                        oColumn.count(theCheck[move][1]) == 3 
                        or oRow.count(theCheck[move][0]) == 3 
                        or {1,2,3}==set(set(oColumn).intersection(oRow)).intersection([1,2,3])
                    ):
                        #used set and intersection
                        await ctx.send("Player O Wins!!")
                        play = True
                    Turn = "X"
                    
        await ctx.send(ticBoard(theBoard))
        if not play:
            await ctx.send("Player '{}'. Move where?".format(Turn))
                
    else:
        await ctx.send("Game is not initiated use *$tic* to initialize your tic tac toe board")

@client.command()
async def resettic(ctx):
    global play,xColumn,xRow,oColumn,oRow,theBoard,Turn,played,theCheck
    played = []
    xColumn = []
    xRow= []
    oColumn= []
    oRow= []

    theBoard = {"t-l":" ","t-m":" ","t-r":" ",
                "m-l":" ","m-m":" ","m-r":" ",
                "b-l":" ","b-m":" ","b-r":" ",}
    Turn = "X"
    play = True
    await ctx.send("Game Reset")
#_______________________end_______________________________


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
async def n(ctx,*mes):
    await ctx.send("https://nhentai.net/g/"+mes[0])

@client.command()
async def randn(ctx):
    n = np.random.randint(000,999)
    await ctx.send("https://nhentai.net/g/325"+str(n))

@client.command()
async def connect(ctx):
    global pl
    global vc
    global ts
    #pl = discord.FFmpegPCMAudio(executable="C:/Users/Sonu/Desktop/SLAM_v1.5.4(1)/ffmpeg.exe", source="sup.mp3")
    print(ctx.author.voice)
    if ctx.author.voice == None:
        await ctx.send("``` Not connected to your AWAZ CHANNEL !! MERI NASS PAT JAOGI MANE VC MEIN JOD!! ```"+ctx.author.mention+" !!")
    else:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        ts = True
        await ctx.send("I am here, I AM HEERREEEEEEEE!! AT "+str(channel))
        #vc.play(pl)
        print(channel, vc)

@client.command()
async def disconnect(ctx):
    global ts
    print(client.voice_clients)
    if len(client.voice_clients)==0:
        await ctx.send("I am not connected to any VC, retarded "+ctx.author.mention+" !!")
    for x in client.voice_clients:
        if len(client.voice_clients)!=0:
            await ctx.send("**SILENT** hojata hu warna mein hi **VIOLENT** hojaunga")
            await x.disconnect()
            ts=False
            

@client.command()
async def play(ctx):    
    global pl
    global vc
    if ts:
        pl = discord.FFmpegPCMAudio(source="./meme/JOJO.mp3")
        vc.play(pl)
    else:
        await ctx.send("Please connect me to any VC!! so I can play your reatarded music (-_-*) ")
    
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
    if ts:
        pl = discord.FFmpegPCMAudio(source="ply.mp3")
        vc.play(pl)
    else:
        await ctx.send("I am not connected nig!! FFS... "+ctx.author.mention+" !!")

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
            pl = discord.FFmpegPCMAudio(source="./songs/"+file)
            vc.play(pl)
    else:
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url,download=True)
        for file in os.listdir('./songs/'):
            if file.startswith(x[:-1]):
                break
        print(file)
        pl = discord.FFmpegPCMAudio( source="./songs/"+file)
        vc.play(pl)    

@client.command()
async def moan(ctx):
    global vc
    global pl
    yi = np.random.randint(0,len(moany))
    print("jaj")
    sor = "./NSFW/"+moany[yi]
    if ts:
        pl = discord.FFmpegPCMAudio( source=sor)
        print("lal")
        vc.play(pl)
    else:
        await ctx.send("FFS let me in the VC!! *DIMAG SE PAIDAL*.. "+ctx.author.mention+" !!")

@client.command()
async def meme(ctx,*me):
    global vc
    global pl
    if ts:
        pl = discord.FFmpegPCMAudio(source="./meme/"+me[0]+".mp3")
        vc.play(pl)
    else:
        await ctx.send("You don't deserve these memes.. "+ctx.author.mention+" !!")

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

import discord
import time

client = discord.Client()


# for jokes
# ------start-----


import numpy as np
import pandas as pd

z = pd.read_csv('jokes.csv')
k = z.iloc[:, 1:2]
y = np.random.randint(0, len(np.array(k)))

# -----end-----

# security------------------
f = open("token.txt", "r")
t = f.read()
f.close()
#---------------------------

@client.event
async def on_ready():
    # await send("swagat ni karoge hamara!!")
    print("UP AND RUNNING".format(client))

stop = False # **
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

    if message.content.startswith('rukja bot'):
        await message.channel.send("hasta-la-vista baby!!:hand_splayed:")
        exit(0)


client.run(t)

import discord

client = discord.Client()

#for jokes
#------start-----

import numpy as np
import pandas as pd

z = pd.read_csv('jokes.csv')
k = z.iloc[:,1:2]
y = np.random.randint(0,len(np.array(k)))

#-----end-----


@client.event
async def on_ready():
    print("UP AND RUNNING".format(client))


@client.event
async def on_message(message):
    global y,l

    if message.author == client.user:
        print("\n yeah same!!")
        return
    if message.content.startswith('$heyo'):
        x = message.content.startswith('$heyo')
        print(x)
        await message.channel.send('\n jhalta hai BSDK!!')
    if message.content.startswith('chammar kon hai'):
        await message.channel.send('chutiya mayank!!')
    if message.content.startswith('god kon hai'):
        await message.channel.send('senpai aap ho SAM THE GOD!!')
    if message.content.startswith('chutiya bot'):
        await message.channel.send('go fuck yourself!! :rage:  :middle_finger: :imp: ')
    if message.content.startswith('wishes'):
        await message.channel.send('happy diwali to you all retards!!:middle_finger: :spy: ')
    if message.content.startswith('jokes') or message.content.startswith('Jokes'):
        y = np.random.randint(0,len(np.array(k)))
        await message.channel.send(np.array(k)[y][0])
    if message.content.startswith('rukja bot'):
        await message.channel.send("hasta-la-vista baby!!:hand_splayed:")
        exit(0)

client.run('NjM3NzAxNDI5NjE1OTE5MTM0.XbSDCQ.X97Iu4NwzkOPeu0VRNMxA594okA')

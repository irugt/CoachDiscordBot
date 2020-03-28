import discord
import json
import time
import threading
from datetime import datetime

class MyClient(discord.Client):

    
    async def on_ready(self):
        print('Logged on as', self.user)
        with open('data.json') as json_file:
            self.data = json.load(json_file)
        print('database loaded')
        await self.checkTime()
        # t = await threading.Thread(target=self.checkTime())
        # await t.start()  

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!ping':
            await message.channel.send('pong!')

        if message.content.startswith('!remind'):

            d = {
                'userId': message.author.id,
                'hour': message.content.split()[1],
                'min': message.content.split()[2],
                'chanId': message.channel.id,
                'message': message
            }
            self.data.append(d)
            await message.channel.send('Your alarm has been set up successfully !')
    
    async def checkTime(self):
        now = datetime.now()
        curH = now.strftime("%H")
        curM = now.strftime("%M")
        print("Current Time =", now.strftime("%H:%M"))
        for d in self.data:
            if (d['hour']==curH) and (d['min']==curM):
                await d['message'].channel.send(d['userId']+", c'est lheure de l'entraînement !")
        time.sleep(59)  


client = MyClient()
client.run('NjkzMjU2MzM5MTc4MTI3NDIw.Xn6bvw.Ae9by0Y1zdG0bSDjM3s2uJxsczs')
import discord
import csv
from pprint import pprint

class Ontobot(discord.Client):

    #conta as mensagens por canal
    async def statistic (self):
        channels = self.get_all_channels()
        total = 0
        response = ""
        for channel in channels:
            try: 
                count = 0
                async for message in channel.history(limit=None):
                    count = count +1
                response = response + "- *"+channel.name + "*: "+str(count) + "\n"
                total = total + count
                    
            except:
                pass
        response = response + "***total: "+ str(total) +"***"
        
        return response
        
    
    #executa sempre que a thread inicia
    async def on_ready(self):
       pprint ("acordado")
    
    async def on_message(self,message):
         if message.content == '#givetotalmessages':
            pprint ("pegando os dados")
            response = await self.statistic()
            await message.channel.send(response)


if __name__ == '__main__':        
    client = Ontobot()
    client.run('<seu token>')

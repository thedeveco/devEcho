import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BotToken')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!ping'):
            await message.channel.send('Pong! :ping_pong:')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

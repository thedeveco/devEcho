import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import importlib

load_dotenv()
TOKEN = os.getenv("BotToken")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    for filename in os.listdir("./src/commands"):
        if filename.endswith(".py"):
            module = f"src.commands.{filename[:-3]}"
            importlib.import_module(module).setup(bot)
    
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

bot.run(TOKEN)

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import importlib
from database.profile import profiledb

load_dotenv()
TOKEN = os.getenv("BotToken")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    for root, _, files in os.walk("./commands"):
        for filename in files:
            if filename.endswith(".py"):
                path = os.path.join(root, filename)
                rel_path = os.path.relpath(path, ".").replace("\\", "/")
                module = rel_path[:-3].replace("/", ".")
                try:
                    importlib.import_module(module).setup(bot)
                    print(f"Loaded {module}")
                except Exception as e:
                    print(f"Failed to load {module}: {e}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

profiledb.init_db()
bot.run(TOKEN)

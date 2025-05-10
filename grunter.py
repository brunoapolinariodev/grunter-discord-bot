# grunter.py  (antigo bot.py)

import os, discord, asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 1️⃣ – carregar extensões no gancho setup_hook
@bot.event
async def setup_hook():
    # Use singular: cogs.general
    await bot.load_extension("cogs.general")
    await bot.load_extension("cogs.tasks")  
    print("✅ cogs carregados")

# 2️⃣ – mensagem friendly quando está pronto
@bot.event
async def on_ready():
    print(f"🐧 Grunter está online como {bot.user}")
    await bot.change_presence(activity=discord.Game("te julgando..."))

if __name__ == "__main__":
    bot.run(TOKEN)

# cogs/general.py
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="oi")
    async def greet(self, ctx):
        await ctx.send("Tsc... oi.")

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))

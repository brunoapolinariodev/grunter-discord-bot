from discord.ext import commands
from utils.persistence import load_tasks, save_tasks

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = []

    async def cog_load(self):
        self.tasks = await load_tasks()

    async def cog_unload(self):
        await save_tasks(self.tasks)

    @commands.command(name="add_task")
    async def add_task(self, ctx, *, task: str):
        self.tasks.append(task)
        await save_tasks(self.tasks)
        await ctx.send(f"Tarefa adicionada: **{task}**")

    @commands.command(name="list_tasks")
    async def list_tasks(self, ctx):
        if not self.tasks:
            await ctx.send("Nenhuma tarefa, preguiçoso.")
        else:
            lista = "\n".join(f"{i+1}. {t}" for i, t in enumerate(self.tasks))
            await ctx.send(f"Suas tarefas:\n{lista}")

    @commands.command(name="del_task")
    async def del_task(self, ctx, index: int):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index-1)
            await save_tasks(self.tasks)
            await ctx.send(f"Removida: **{removed}** (espero que tenha feito!)")
        else:
            await ctx.send("Índice inválido.")

async def setup(bot):
    await bot.add_cog(Tasks(bot))

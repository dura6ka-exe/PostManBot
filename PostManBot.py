import discord
from discord.ext import commands
import asyncio

BOT_TOKEN = 'TOKEN'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user.name}')

@bot.command()
async def start(ctx, count: int, *, message: str = "starting"):
    if ctx.author.id == bot.user.id:
        return

    if not ctx.guild:
        await ctx.send("Эту команду можно использовать только на сервере!")
        return

    if count <= 0 or count > 200:
        await ctx.send("Количество сообщений должно быть больше 0 и не превышать 200.")
        return

    members = [m for m in ctx.guild.members if not m.bot]

    for member in members:
        for i in range(count):
            await member.send(f'{message}')
            await asyncio.sleep(0.5)

    await ctx.send(f'Отправил {count} сообщений каждому участнику сервера с текстом: "{message}".')

bot.run(BOT_TOKEN)

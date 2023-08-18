import discord
import webbrowser
import os, random
from discord.ext import commands

version = 1.2

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
#RR
items = {
    'бумага': ['2 года', 'пункт приема макулатуры у населения', 'https://rimtest.ru/wp-content/uploads/Ofisnaya-bumaga.jpg', 'https://ru.wikipedia.org/wiki/%D0%91%D1%83%D0%BC%D0%B0%D0%B3%D0%B0'],
    'пластик': ['от 6 месяцев до 700 лет ', ' городские пункты приема вторсырья', 'https://www.ixbt.com/img/n1/news/2018/3/4/d_large.jpg', 'https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%B0%D1%81%D1%82%D0%BC%D0%B0%D1%81%D1%81%D1%8B']

}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def help(ctx):
    await ctx.send('/mem -- мемы; /info материал -- информация')

@bot.command()
async def version(ctx):
    await ctx.send(f'Версия бота: {version}')

@bot.command()
async def mem(ctx):
    list_sam = os.listdir('mems')
    img_name = random.choice(list_sam)
    with open(f'mems/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def info(ctx, item):
    lowitem = item.lower()
    webbrowser.open_new(items[lowitem][3])
    if lowitem in items:
        await ctx.send(items[lowitem][2])
        await ctx.send(f'Кратко: {lowitem} разлагается {items[lowitem][0]}. Можно сдать в {items[lowitem][1]}')
    else:
        await ctx.send('Материал не найден')

bot.run('MTEzMjI3NzQxMDYzNzgyNDA1MQ.G2-y_J.PN1Z4e7ibAvFUzOItELQEvmPG4UQaJPILXZPoo')
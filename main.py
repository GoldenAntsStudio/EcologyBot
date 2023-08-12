import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
#RR
items = {
    'бумага': ['2 года', 'пункт приема макулатуры у населения', 'https://rimtest.ru/wp-content/uploads/Ofisnaya-bumaga.jpg'],
    'пластик': ['от 6 месяцев до 700 лет ', ' городские пункты приема вторсырья', 'https://www.ixbt.com/img/n1/news/2018/3/4/d_large.jpg']

}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def info(ctx, item):
    lowitem = item.lower()
    if lowitem in items:
        await ctx.send(items[lowitem][2])
        await ctx.send(f'{lowitem} разлагается {items[lowitem][0]}. Можно сдать в {items[lowitem][1]}')
    else:
        await ctx.send('Материал не найден')

bot.run('MTEzMjI3NzQxMDYzNzgyNDA1MQ.G2-y_J.PN1Z4e7ibAvFUzOItELQEvmPG4UQaJPILXZPoo')
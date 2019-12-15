import asyncio,discord,os
from dicebot import *

client = discord.Client()

PopularDices=['1d100','1d10','3d6','2d6','1d6','1d4','2d3','1d3','1d20','1d30']
Channels=["dice","ダイス"]
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #--character--
    if message.content.startswith('!character make'):
        await message.channel.send(f'{message.author.mention} ' +str(character.make()))
    if message.content.startswith('!character load'):
        index = message.content.replace("!character load ","")
        await message.channel.send(f'{message.author.mention} ' +str(character.load(index)))
    """
    if message.content.startswith('!help'):
        await message.channel.send("Dicebot\n!character make - 簡単なキャラメイクができます.\n")
    """

    #--dice--
    if message.channel.name in Channels:
        try:
            n,d = map(int,message.content.split('d'))
        except ValueError:
            await message.channel.send(f"{message.author.mention}正しいフォーマットで入力してください.")
        else:
            await message.channel.send(f'{message.author.mention} result : '+ str(dice.roll(n,d)))
        

client.run(os.environ["SECRET_TOKEN"])
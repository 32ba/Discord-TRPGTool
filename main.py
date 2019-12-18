import asyncio,discord,os
from dicebot import *

client = discord.Client()

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
    try:
        #--character--
        if message.content.startswith('!character make'):
            await message.channel.send(f'{message.author.mention} ' +str(character.make()))
            await message.guild.create_text_channel("channelName")
        if message.content.startswith('!character load'):
            index = message.content.replace("!character load ","")
            await message.channel.send(f'{message.author.mention} ' +str(character.load(index)))

        #--help--
        if message.content.startswith('!help'):
            return

        #--dice--
        if message.channel.name in Channels:
            try:
                n,d = map(int,message.content.split('d'))
            except ValueError:
                return
            else:
                await message.channel.send(f'{message.author.mention} result : '+ str(dice.roll(n,d)))
    except discord.errors.Forbidden:
        await message.channel.send("権限不足です。\n新しく追加された機能を使う際、Botの再連携が必要な場合があります。\n詳しくは下記のURLを参照してください。\nhttps://github.com/32ba/TRPGTool/README.md")
        

client.run(os.environ["SECRET_TOKEN"])
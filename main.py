import discord
import os
from dotenv import load_dotenv
from inspire import get_quote
from joke import get_joke
from photos import get_photo
from search import search
from duckduckgo_search import ddg_translate

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)


KEY = os.environ.get(str('TOKEN'))

prefix = '$'

@client.event
async def on_ready():
    print("We have logged in as", client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '$inspire' and message.channel.name == 'get_inspired':
        quote = "Quote for " + message.author.mention + '\n' + get_quote()
        await message.channel.send(quote)
        return
        
    if message.content == '$joke' and message.channel.name == 'jokes':
        await message.channel.send(get_joke())
        return

    if message.content == '$invite':
        invite = await message.channel.create_invite()
        await message.channel.send(f'Here is the invite link for the server: {invite.url}')
        return
    
    if message.content.startswith('$photo'):
        query = message.content.split('$photo ')[1]
        await message.channel.send(get_photo(query))

    if message.content.startswith('$search'):
        query = message.content[8:]
        response = search(query)[1] + '\n' + search(query)[2] + '\n' + search(query)[0]
        await message.channel.send(response)
        return
    
    if message.content.startswith('$t'):
        keywords = message.content[3:]
        response  = ddg_translate(keywords, to = 'en')
        await message.channel.send(response[0]['translated'])
        return

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcome')
    await channel.send(f"Hi! Bud {member.mention}, Welcome to our server.")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='good_bye')
    await channel.send(f"Bye! Bud {member.mention}, We will miss u :(")


client.run(KEY)

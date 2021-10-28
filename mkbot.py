import discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix = '.')

#onoff
@client.event
async def on_ready():
    print('bot is ready')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('defrosting, 0.3%'))

#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)}ms')

client.run('OTAzMzY0MzUwMzgxODAxNDgy.YXr5nA.6f3Cw-O6fEO6hOw2uU7p5PPAkZ8')
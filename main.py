import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is logged in and ready!')
    print(f'User: {client.user}')
    print(f'ID: {client.user.id}')
    print('------------------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello! I am online and ready for n8n.')

try:
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if token is None:
        print("ERROR: DISCORD_BOT_TOKEN environment variable not set.")
    else:
        client.run(token)
except discord.errors.LoginFailure:
    print("ERROR: Improper token has been passed.")


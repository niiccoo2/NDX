import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot is ready. Connected as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'ping':
        await message.channel.send('Pong!')

client.run('MTExNTc1Mzg2MDM2Mzk4MDg4MQ.GHGeUv.TaG_-7MIlw5CKtX0TW7iu-h3CNJQYc9oDlqL7Q')

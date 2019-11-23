import discord
from discord.ext import commands

def get_prefix(client,message):
    with open('prefixes.json', 'r')as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)

extensions_initiales=["cogs.modération"]


if __name__ == '__main__':
    for extension in extensions_initiales:
        bot.load_extension(extension)

client.remove_command('help')
@client.event
async def on_ready():
    print(f'\n\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')
    print(f'Connected!')
    
bot.run(TOKEN)

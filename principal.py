import discord
from discord.ext import commands
client = commands.Bot(command_prefix= "!")


extensions_initiales=["cogs.modération"]


if __name__ == '__main__':
    for extension in extensions_initiales:
        bot.load_extension(extension)

bot.remove_command('help')
@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Connected!')
    
bot.run(TOKEN)

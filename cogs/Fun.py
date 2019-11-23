import discord 
from discord.ext import commands
import random 

class fun(commmands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def ping(self,ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Color.dark_blue())
    embed.add_field(name="Ping ?", value="Pong :ping_pong:")
    embed.add_field(name="Latence en ms :", value=(client.latency * 1000))
    await ctx.send(author, embed=embed)

@commands.command(name='8ball',
                description="Répond a une question par oui ou par non",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(ctx):
    possible_responses = [
        "C'est un non retentissant",
        "Ce n'est pas probable",
        'Trop difficile à dire',
        "C'est possible",
        "Définitivement",
        "Je ne pense pas",
        "Bien sûr",
        "Certainement pas",
        "Je ne peux pas le prédire ",
        "Mes sources disent que non",
        "Ma réponse est non",
        "Concentrez-vous et reposez-moi une question ",
        "Oui, définitivement",
        "Demandez-moi plus tard",
        "Essayez encore une fois pour voir ?",
        "Aucun doute possible",
        "Je pense que oui",
    ] 
    await ctx.send(f"{ctx.author.mention}{random.choice(possibles_reponses)})
@commands.command()
async def serveur(self, ctx):
  	embed = discord.Embed(title=f"{ctx.guild.name}", color=discord.Color.blue())
  	embed.add_field(name="Serveur crée le :", value= ctx.guild.created_at)
  	embed.add_field(name="Créateur du serveur :", value= ctx.guild.owner)
  	embed.add_field(name="Région du serveur :", value=ctx.guild.region )
  	embed.add_field(name="Id du serveur :", value= ctx.guild.id)
  	embed.add_field(name="Nombre de personnes sur le serveur :",value=f"{len(ctx.guild.members)})
    embed.set_thumbnail(url =ctx.guild.icon_url)
  	roles = ctx.guild.roles
  	for role in roles:
  		embed.add_field(name= "Roles du serveur", value= role )
  	await ctx.send(embed=embed)


@client.command()
async def bingo(ctx, num1 : int):
    if not num1:
        embed = discord.Embed(title="Bingo Erreur", colour=discord.Color.dark_blue())
        embed.add_field(name=f"Erreur :", value=f"Vous devez indiquer un chiffre après la commande ") 
        await ctx.send(embed=embed)
    else:
        nb = random.randint(1,num1)
        essaie = 0
        print(nb)
        embed = discord.Embed(title="Bingo", colour=discord.Color.dark_blue())
        embed.add_field(name=f"Bingo lancé", value=f"Le nombre a trouvé est entre 1 et {num1}") 
        await ctx.send(embed=embed)
        while boucle == 0:
            message = await client.wait_for('message')
            jsp = message.content
            nombre = int(jsp)
            if nombre == nb:
                par = ctx.author.mention
                par2 = ctx.message.author.mention
                embed = discord.Embed(title="Bingo", colour=discord.Color.dark_blue())
                embed.add_field(name="Bingo gagné", value=f"Le nombre a été trouvé par {par} !")
                embed.add_field(name="La réponse était :", value=f"{nb}")
                embed.add_field(name=f"Tu a trouvé le nombre mystère en :", value=f"{essaie} essaies")
                await ctx.send(embed=embed)
                break

            if nombre > nb:
                await ctx.send("C'est plus petit")
                essaie += 1
            elif nombre < nb:
                await ctx.send("C'est plus grand !")
                essaie +=1

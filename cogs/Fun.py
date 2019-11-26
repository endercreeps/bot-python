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
                description="Répond a une question par oui ou par non")
async def eight_ball(self,ctx):
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
    await ctx.send(f"{random.choice(possibles_reponses)}, {ctx.author.mention}")
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
	@commands.command()
	async def bingo(self,ctx, numb1: int):
		nb = random.randint(1,numb1)
		essaie = 0
		print(nb)
		embed = discord.Embed(color = discord.Color.dark_blue(), title = "BINGO lancé !", description = f"Le nombre a trouvé est entre 1 et {numb1}.\nBonne chance !")
		await ctx.send(embed=embed)
		while True:
			def check(si):
				return si.author == ctx.message.author
			message1 = await self.bot.wait_for('message', check = check)
			msg = int(message1.content)
			if msg == nb:
				embed = discord.Embed(title="Bingo gagné !",description = f"le nombre a été retrouvé par **{ctx.message.author}**.\n Le nombre a trouvé était: **{nb}**.\n{ctx.message.author} a retrouvé le nombre mystère en: **{essaie}** essaies.", colour=discord.Color.dark_blue())
				await ctx.send(embed=embed)
				break
			if msg > nb:
				await ctx.send("C'est plus petit !")
				essaie += 1 
			elif msg < nb:
				await ctx.send("C'est plus grand !")
				essaie +=1
	@bingo.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed = discord.Embed(title="Bingo Erreur",description = "vous devez indiquer un nombre ou un chiffre après la commande. " ,colour=discord.Color.red())
			await ctx.send(embed=embed)


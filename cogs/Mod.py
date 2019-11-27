import discord 
from discord.ext import commands
import random 

class modération(commmands.Cog):
  def __init__(self, bot):
    self.bot = bot

from fonction import *

@commmands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Pas de raison"):
    await ctx.channel.purge(limit=1)
    channel = discord.utils.get(member.guild.channels, name="privé")
    par = ctx.author.name
    qui = member.name
    if not member:
        await ctx.send("**Merci de donner le nom de l'utilisateur**")
        return
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kick", colour=000000)
    embed.add_field(name=f"Vicime :", value=(qui))
    embed.add_field(name=f"Raison du kick :", value=(reason))
    embed.add_field(name=f"Par:", value=(par))
    #await ctx.channel.send(embed=embed)
    await ctx.send(embed=embed)
    await ctx.create_dm()
    await ctx.dm_channel.send(embed=embed)
    print("Une personne a été kick")

@commmands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Pas de raison"):
    await ctx.channel.purge(limit=1)
    channel = discord.utils.get(member.guild.channels, name="privé")
    par = ctx.author.name
    qui = member.name
    if not member:
        await ctx.send("**Merci de donner le nom de l'utilisateur**")
        return
    await member.ban()
    embed = discord.Embed(title="Ban", colour=000000)
    embed.add_field(name=f"Vicime :", value=(qui))
    embed.add_field(name=f"Raison du ban :", value=(reason))
    embed.add_field(name=f"Par :", value=(par))
    await ctx.send(embed=embed)
    await member.create_dm()
    await member.dm_channel.send(embed=embed)
    print("Une personne a été ban")

@commmands.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason="Pas de raison"):
    await ctx.channel.purge(limit=1)
    channel = discord.utils.get(member.guild.channels, name="privé")
    role_mute = discord.utils.get(ctx.guild.roles, name="Muted")
    par = ctx.author.name
    qui = member.name
    if not member:
        await ctx.send("**Merci de donner le nom de l'utilisateur**")
        return 
    await member.add_roles(role_mute)
    embed = discord.Embed(title="Mute", colour=000000)
    embed.add_field(name=f"Vicime :", value=f"{qui}")
    embed.add_field(name=f"Raison du mute :", value=f"{reason}")
    embed.add_field(name=f"Par :", value=f"{par}")
    await ctx.send(embed=embed)
    await member.create_dm()
    await member.dm_channel.send(embed=embed)
    print("Une personne a été mute")

@commmands.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member=None):
    await ctx.channel.purge(limit=1)
    channel = discord.utils.get(member.guild.channels, name="privé")
    role_mute = discord.utils.get(ctx.guild.roles, name="Muted")
    par = ctx.author.name
    qui = member.name
    if not member:
        await ctx.send("**Merci de donner le nom de l'utilisateur**")
        return 
    await member.remove_roles(role_mute)
    embed = discord.Embed(title="Unmute", colour=000000)
    embed.add_field(name=f"Vicime :", value=f"{qui}")
    embed.add_field(name=f"Mute enlevé par :", value=f"{par}")
    await ctx.send(embed=embed)
    await member.create_dm()
    await member.dm_channel.send(embed=embed)
    print("Une personne a été unmute")


@commmands.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="Clear", colour=000000)
    embed.add_field(name="Nombre de messages supprimés", value= amount)
    await ctx.send(embed=embed)
    time.sleep(2)
    await ctx.channel.purge(limit=1)
    print("Des messages on été suprimés")

@commmands.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  await ctx.channel.purge(limit=1)
  for current_user in report['users']:
    if user.name == current_user['name']:
        await ctx.send(f"```{user.name} a été warn: {len(current_user['reasons'])} fois pour : {','.join(current_user['reasons'])}```")
        break
    else:
        await ctx.send(f"```{user.name} n'a jamais été warn```")

@commmands.command(pass_context = True)
@has_permissions(manage_roles=True, kick_members=True)
async def warn(ctx, id:discord.User,*reason:str):
  await ctx.channel.purge(limit=1)
  par = ctx.author.name
  guild = ctx.message.guild
  if not reason:
    await client.say("**Merci de mettre une raison**")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)
    await member.create_dm()
    await member.dm_channel.send(f"**Hey** {user.mention} **! Vous vous êtes warn sur {guild} :0 pour :** {reason} ")
    embed = discord.Embed(title="Warn", colour=000000())
    embed.add_field(title="Victime :", value=f"{user.name}")
    embed.add_field(name=f"Raison du warn :", value=f"{reason}")
    embed.add_field(name=f"Par :", value=f"{par}")
    await ctx.send(embed=embed)
    print("Une personne a été warn")

#@commmands.command()
#@commands.has_permissions(ban_members=True)
#async def add_blacklist(ctx, user: str, id:int):
 #    with open('blacklist.json', 'r')as f:
  #      blacklist = json.load(f)
#
 #       blacklist[str(user)] = [id]
  #      with open('blacklist.json', 'w')as f:
   #         json.dump(blacklist, f, indent=4)
#
 #       await ctx.send(f"L'utilisateur {user} avec l'id ``{id}`` a été ajouté à ma blacklist avec succès")

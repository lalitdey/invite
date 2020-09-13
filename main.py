import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import time
prefix = "+"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="owner"

@bot.event
    print(bot.user.name)
    

@bot.command(name="++")
#@commands.has_role('owner')
async def f(ctx,*,msg):
	await ctx.message.delete()
	author=ctx.message.author
	
	for guild in bot.guilds:
		for member in guild.members:
			try:
				await member.send(msg)
				embed=discord.Embed(title="DISCORD MASS DM",description=f"DM sent to {member.name} \n:white_check_mark:",colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				embed.set_thumbnail(url = member.avatar_url)
				
				await ctx.send(embed=embed)
			except:
				embed=discord.Embed(title='''DISCORD MASS DM''',description=f'''DM Not sent to {member.name}#{member.discriminator}''' ''' :x: ''',colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				embed.set_thumbnail(url = member.avatar_url)
				
				await ctx.send(embed=embed)
					
        
bot.run("NzU0NjYxMzIwNDM5MTAzNDk4.X13_Hw.7oby7M00mxtxOMYAkOaiyo-QMVw")  # Where 'TOKEN' is 

import discord
from discord.ext import commands

# creates discord bot, sets command_prefix as !
bot = commands.Bot(command_prefix='!', description='A bot that greets the user back.')

# when bot logs in it will send a message with name and id
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# bot takes two integers and addes them together
@bot.command()
async def add(ctx, a: int, b: int):
	await ctx.send(a+b)

# bot takes two integers and multiples them together
@bot.command()
async def multiply(ctx, a: int, b: int):
	await ctx.send(a*b)

# bot greets you with lil wayne lyrics
@bot.command()
async def realgs(ctx):
	await ctx.send("real Gs move in silence like lasagna")

# classic mom command
@bot.command()
async def mom(ctx):
	await ctx.send("Roast me all you want but once you mention my mom then shit gets me heated a bit")

# drug island
@bot.command()
async def drugisland(ctx):
	await ctx.send("HEADLINERS: Kendrick Lamar, Marshmello, Diplo b2b Major Lazer b2b Jack U, J Cole, Bassnectar, Snoop Dogg, Kid Cudi and more to come!")

# bot blesses the rains down in africa
@bot.command()
async def africa(ctx):
    await ctx.send("https://media.giphy.com/media/13LNbx6Tvlxej6/giphy.gif")

# bot gives you details on who made the bot
@bot.command()
async def info(ctx):
	embed = discord.Embed(title="Dev Discord Bot", description="I'm just a stupid bot.", color=0xeee657)

	# give info about me here
	embed.add_field(name="Author", value="yeezy")

	# show the number of servers the bot is a member of.
	embed.add_field(name="Server count", value=F"{len(bot.guilds)}")

	await ctx.send(embed=embed)

# discord.py generates a help command automatically. this removes the one given by it.
bot.remove_command('help')

# runs bot using token 
bot.run('token')
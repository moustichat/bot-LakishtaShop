#coding:utf-8


import discord


number_of_member = 5
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents = default_intents)



	
@client.event
async def on_ready():
		print("Le bot est prêt")

@client.event
async def on_member_join(member):
	general_channel: discord.TextChannel = client.get_channel(920672338561880145)
	await general_channel.send(content = f"Bienvenue sur le serveur de **{member.guild.name}** {member.mention} ! \U0001F604 ")


@client.event
async def on_member_remove(member):
	general_channel: discord.TextChannel = client.get_channel(920672338561880145)
	await general_channel.send(content = f"Oh non, {member.mention} est parti \U0001F622 ")

@client.event
async def on_message(message):
	if message.content.startswith("!del"):
		number = int(message.content.split()[1])
		messages = await message.channel.history(limit = number + 1).flatten()

		for each_message in messages:
			await each_message.delete()


client.run("OTIwNjcyMTQxOTUzODcxODgy.Ybnwvw.meTHddMfJjiNSGpL4ddW22FSN0o")
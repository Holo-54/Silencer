# import libraries
import discord
import random
import asyncio
from discord import app_commands

# bot configuration
intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)

# -------------------------------------------------
# FUNCTIONS, FILES, AND IMPORTANT VARIABLES
# -------------------------------------------------

# API Token
a = open('./API_Token.txt','r')
api_token = a.read()
a.close()



# -------------------------------------------------
# INITIALIZATION
# -------------------------------------------------
client.run(api_token)
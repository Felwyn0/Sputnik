import discord

import datetime #for timecodes... maybe


from redbot.core import commands, app_commands
from enum import Enum

#used in command 2, "testarg"
class Args(Enum):
    One = "1"
    Two = "2"
    Three = "3"

class attendtest(commands.Cog):
    """test"""
    def __init__(self, bot):
        self.bot = bot

#command 1
    @app_commands.command(name="command-test")
    async def test1(self, interaction: discord.Interaction):
        """simple call and response"""
        # Your code will go here
        await interaction.response.send_message("test", ephemeral=True)


#command 2
    @app_commands.command(name="arg-test")
    @app_commands.describe(arggroup="description of what the choice means")
    async def test2(self, interaction: discord.Interaction, arggroup: Args):
        """less simple, choice of arguments"""
        # Your code will go here
        await interaction.response.send_message(f"chosen arg is {arggroup.value}", ephemeral=True)
        
#command 3
#    @app_commands.command(name=
#    @app_commands.describe(
#    async def testint(self, interaction: discord.Interaction):
#        """integrated reactions?"""
#        # code here
#        await interaction.response.send_message("awa", ephemeral=True)
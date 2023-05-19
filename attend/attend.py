import discord
from redbot.core import commands, app_commands
from enum import Enum

class Roles(Enum):
    Owner = "owner"
    Dancer = "dancer"


class attendtest(commands.Cog):
    """test"""
    def __init__(self, bot):
        self.bot = bot

#command 1
    @app_commands.command()
    async def test(self, interaction: discord.Interaction):
        """simple call and response"""
        # Your code will go here
        await interaction.response.send_message("test", ephemeral=True)


#command 2
    @app_commands.command(name="awa")
    @app_commands.describe(roles="role to sign up as")
    async def testint(self, interaction: discord.Interaction, test1: Roles):
        """less simple, interaction decision"""
        # Your code will go here
        await interaction.response.send_message("role is {test1.value}", ephemeral=True)
        
        
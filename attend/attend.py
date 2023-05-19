import discord
from redbot.core import commands, app_commands

class attendtest(commands.Cog):
    """test"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def test(self, interaction: discord.Interaction):
        """simple call and response"""
        # Your code will go here
        await interaction.response.send_message("test", ephemeral=True)
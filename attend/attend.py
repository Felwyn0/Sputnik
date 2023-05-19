from redbot.core import commands

class attendtest(commands.Cog):
    """test"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """simple call and response"""
        # Your code will go here
        await ctx.send("pong")
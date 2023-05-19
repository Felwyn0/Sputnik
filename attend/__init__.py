from .attend import attendtest


async def setup(bot):
    bot.add_cog(attendtest(bot))
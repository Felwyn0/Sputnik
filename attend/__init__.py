from .attend import attendtest

async def setup(bot):
    await bot.add_cog(attendtest(bot))
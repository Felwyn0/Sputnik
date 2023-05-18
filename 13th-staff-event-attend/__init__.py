from .attend import 13th_attendtest


async def setup(bot):
    await bot.add_cog(13th_attendtest(bot))
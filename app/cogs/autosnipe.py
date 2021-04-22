import typing

import discord
from discord.ext import commands

if typing.TYPE_CHECKING:
    from app.bot import AutoSnipe


class Sniper(commands.Cog):
    def __init__(self, bot: "AutoSnipe"):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        await message.channel.send(
            f"{message.author}: {message.system_content or '*file only*'}"
        )


def setup(bot: "AutoSnipe"):
    bot.add_cog(Sniper(bot))

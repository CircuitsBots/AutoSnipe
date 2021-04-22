from discord.ext import commands


class AutoSnipe(commands.Bot):
    async def on_command_error(self, ctx: commands.Context, exc: Exception):
        await ctx.send(exc)

    def run(self, *args, **kwargs):
        self.load_extension("app.cogs.autosnipe")
        return super().run(*args, **kwargs)

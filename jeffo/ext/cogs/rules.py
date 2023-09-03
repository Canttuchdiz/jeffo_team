from __future__ import annotations
from discord import TextChannel, Embed
from discord.ext import tasks
from discord.ext.commands import Bot, Cog, command, Context, has_permissions
from jeffo.utils.constants import Embeds


class Rules(Cog):

    def __init__(self, bot: Bot) -> None:
        self.client = bot

    @command(name="rules")
    @has_permissions(administrator=True)
    async def send_rules(self, ctx: Context) -> None:
        embed = Embed.from_dict(Embeds.rules)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Rules(bot))

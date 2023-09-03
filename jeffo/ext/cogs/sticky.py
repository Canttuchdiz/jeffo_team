from __future__ import annotations
import asyncio
from discord import TextChannel
from discord.ext import tasks
from discord.ext.commands import Bot, Cog, command, Context, has_permissions
from jeffo.utils.constants import StickyMessages
from typing import List
import datetime


class Sticky(Cog):

    def __init__(self, bot: Bot) -> None:
        self.client = bot

    @tasks.loop(minutes=4)
    async def bot_update(self, channel: TextChannel) -> None:
        await channel.send(StickyMessages.amMessage[0])
        await asyncio.sleep(120)
        await channel.send(StickyMessages.amMessage[1])

    @command(name="start")
    @has_permissions(administrator=True)
    async def start(self, ctx: Context) -> None:
        await ctx.send("Started!")
        self.bot_update.start(ctx.channel)


async def setup(bot):
    await bot.add_cog(Sticky(bot))

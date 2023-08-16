from __future__ import annotations
import asyncio
from discord import TextChannel, Message
from discord.ext import tasks
from discord.ext.commands import Bot, Cog, command, Context, has_permissions
from jeffo.utils.constants import WFLEmojis
from typing import List
import datetime


class WFL(Cog):

    def __init__(self, bot: Bot) -> None:
        self.client = bot

    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        if message.channel.id in WFLEmojis.channels and WFLEmojis.trigger in message.content:
            for emoji in WFLEmojis.wfl:
                await message.add_reaction(self.client.get_emoji(emoji))


async def setup(bot):
    await bot.add_cog(WFL(bot))

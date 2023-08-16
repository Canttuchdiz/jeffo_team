from __future__ import annotations
import asyncio
from discord import TextChannel, Message
from discord.ext import tasks
from discord.ext.commands import Bot, Cog, command, Context, has_permissions
from jeffo.utils.constants import BannedPhrases
from jeffo.utils.logging import Logging
from typing import List
import datetime


class Phrases(Cog):

    def __init__(self, bot: Bot) -> None:
        self.client = bot

    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        for phrase in BannedPhrases.phrases:
            if phrase.lower() in message.content.lower():
                logging_channel = self.client.get_channel(BannedPhrases.log_channel)
                reason = f"Sent message containing banned phrase"
                embed = Logging.ban_log(message.author, reason)
                await logging_channel.send(embed=embed)
                await message.author.ban(reason=reason)


async def setup(bot):
    await bot.add_cog(Phrases(bot))

from pathlib import Path
from dotenv import load_dotenv
import discord
from discord import Color
from discord.ext import commands
import os
import traceback
import sys

MY_DIR = Path(__file__).parent

load_dotenv()

TOKEN: str = str(os.environ["TOKEN"])

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.bans = True


class Bot(commands.Bot):

    # Initializes needed data
    def __init__(self) -> None:
        super().__init__(command_prefix='!', intents=intents,
                         activity=discord.Activity(name="Jeffo",
                                                   type=discord.ActivityType.watching),
                         status=discord.Status.dnd)

    # def exception_handler(exctype, value, traceback):
    #     except AttributeError:
    #         raise InvalidTable
    #
    #     sys.__excepthook__(exctype, value, traceback)

    # Loading all cogs
    async def setup_hook(self) -> None:

        # sys.excepthook = self.exception_handler
        for filename in os.listdir(MY_DIR / "ext/cogs"):
            if os.path.isfile(os.path.join(MY_DIR / "ext/cogs", filename)):

                try:
                    if filename.endswith(".py"):
                        cog = f"jeffo.ext.cogs.{filename[:-3]}"
                        await self.load_extension(cog)
                except Exception as e:
                    print(f"Failed to load cog {filename}")
                    traceback.print_exc()
        await self.load_extension('jishaku')


# Creates instance of the bot and then runs it
client = Bot()
client.remove_command('help')
client.total_rules = 0


@client.command()
@commands.is_owner()
async def reload(ctx, cog_name) -> None:
    """Reloads a cog"""
    try:
        await client.reload_extension(f"jeffo.ext.cogs.{cog_name}")
        await ctx.send(f"Reloaded cog: {cog_name}")
    except Exception as e:
        await ctx.send(f"Error: {e}")


client.run(TOKEN)
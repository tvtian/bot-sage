from typing import Counter
import discord
import asyncio
from discord import channel
from discord.ext import commands
from discord.utils import SequenceProxy
from core.classes import Cog_Extension


class task(Cog_Extension):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(896254827108118538)
            sec = 0
            sec1 = 0
            Min = 0
            min1 = 0
            hr = 0
            hr1 = 0
            while not self.bot.is_closed():
                if sec == 10:
                    sec = 0
                    sec1 += 1
                if sec1 == 6:
                    sec1 = 0
                    Min += 1
                if Min == 10:
                    Min = 0
                    min1 += 1
                if min1 == 6:
                    min1 = 0
                    hr += 1
                if hr == 10:
                    hr = 0
                    hr1 += 1
                await self.channel.send(f'Bot 已運行 {hr1}{hr}:{min1}{Min}:{sec1}{sec}')
                print(f'Bot 已運行 {hr1}{hr}:{min1}{Min}:{sec1}{sec}')
                sec += 1
                await asyncio.sleep(1)


        self.bg_task = self.bot.loop.create_task(interval())


def setup(bot):
    bot.add_cog(task(bot))
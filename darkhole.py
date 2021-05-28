#!/usr/bin/env python3

from datetime import datetime
import logging
import os

from discord.ext import commands
import discord

# Configure logging
logger = logging.getLogger(name='DarkHole')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename=f'DarkHole_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log',
    encoding='utf-8',
    mode='w'
)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Get channel ID
channel_id = os.getenv('CHANNEL_ID')


def is_void(message) -> bool:
    logger.info(f'`void` called in channel with ID: {message.channel.id}')
    return False if not channel_id else message.channel.id == channel_id


@commands.command(name='void')
async def void(ctx, num_messages: int = 1) -> None:
    deleted_messages = await ctx.channel.purge(limit=num_messages, check=is_void)
    if not deleted_messages:  # If the list is empty
        logger.info('No messages to delete.')
        return None
    async with ctx.channel.typing():
        with open('DarkHole.png', 'rb') as f:
            card = discord.File(f)
            await ctx.channel.send(
                f'I activate **Dark Hole**! All {len(deleted_messages)} messages have been sent to the graveyard!',
                file=card,
                delete_after=60.0
            )


@commands.command(name='set')
async def set_channel(ctx, channel: int = None) -> None:
    global channel_id
    channel_id = channel
    return None

if __name__ == '__main__':
    # Configure bot
    bot = commands.Bot(
        command_prefix='>',
        description='That does what it do!'
    )
    token = os.getenv('AUTH_TOKEN')
    if not token:
        exit(f'Could not authenticate. Value of `token` is: {token}')

    bot.add_command(void)
    bot.add_command(set_channel)
    bot.run(token)

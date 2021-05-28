# Dark Hole

Yell into the void, I'll delete the messages!

## Requirements

Python 3.9+, `discord.py`, and patience.

For development, we use [`pipenv`](https://pipenv.pypa.io/en/latest/)
to manage our development environment.

### Bot usage

The Discord authentication token is taken from an environment variable,
`AUTH_TOKEN`. If this variable does not exist then the bot will not run.

You can also store the channel ID you would like to set the bot to use
with an environment variable, `CHANNEL_ID`. You can also provide it with
the `set` command.

Commands begin with a `>`.

To delete messages, send `>void <n>` where `n` is the number of messages
you would like to delete.

To set a channel for the bot to operate in, use the `set` command.
`>set <CHANNEL_ID>` will set the bot to operate in that channel. You can
get the channel ID by right-clicking on a channel in Discord and
clicking "Copy ID".

The bot can only operate in one channel at a time, in order to prevent
chaos, since anyone can run the `void` command.
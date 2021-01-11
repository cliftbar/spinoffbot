from datetime import datetime, timedelta
from typing import List

import pytz
from discord import Message, Guild, TextChannel, Client
from discord.abc import GuildChannel

from models import FirestoreSpinoffModel, ChannelDocument


class SpinoffBot:
    def __init__(self, client: Client, channel_prefix: str = "spinoff"):
        self.client: Client = client
        self.channel_prefix: str = channel_prefix

        self.model = FirestoreSpinoffModel()

    async def spinoff_channel(self, message: Message) -> None:
        message_parts: List[str] = message.content.split(maxsplit=1)
        title: str = message_parts[1]
        title_safe: str = title.strip().lower().replace(' ', "_")
        server: Guild = message.guild

        new_channel: TextChannel = await server.create_text_channel(f"{self.channel_prefix}_{title_safe}")
        await new_channel.send("Welcome to the spinoff channel")
        self.model.store_spinoff_channel(new_channel)

    async def clean_spinoff_channels(self) -> None:
        stale_channel_cutoff: timedelta = timedelta(days=1)
        stale_now: datetime = datetime.now(tz=pytz.utc)
        channels: List[TextChannel] = self.get_channels()
        for channel in channels:
            if stale_channel_cutoff < (channel.created_at - stale_now):
                await channel.delete()
            last_message: Message = self.get_last_message(channel)
            if stale_channel_cutoff < (last_message.created_at - stale_now):
                await channel.delete()

    def get_channels(self) -> List[TextChannel]:
        channels: List[ChannelDocument] = self.model.get_channels()
        return [self.client.get_channel(c.id) for c in channels]

    def get_last_message(self, channel: TextChannel) -> Message:
        return channel.last_message


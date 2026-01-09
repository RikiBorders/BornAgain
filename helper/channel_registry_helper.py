from typing import Optional

class ChannelRegistryHelper:
    
    def __init__(self):
        # channels are null by default.
        self.channels: dict[str, Optional[int]] = {
            "welcome": None,
            "command": None
        }

    def channel_is_registered(self, channel_type: str) -> bool:
        return self.channels.get(channel_type) is not None
    
    def register_channel(self, channel_type: str, channel_id: int):
        if channel_type in self.channels:
            self.channels[channel_type] = channel_id
        else:
            raise ValueError(f"Unknown channel type: {channel_type}")

    def get_channels(self):
        return self.channels
    
    def get_channel(self, channel_type: str) -> Optional[int]:
        self.channels.get(channel_type)
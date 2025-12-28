

class ChannelRegistryHelper:
    
    def __init__(self):
        # channels are null by default.
        self.channels = {
            "welcome": None,
            "command": None
        }

    def channel_is_registered(self, channel_type: str) -> bool:
        return self.channels.get(channel_type) is not None
    
    def register_channel(self, channel_type: str, channel_id):
        if channel_type in self.channels:
            self.channels[channel_type] = channel_id
        else:
            raise ValueError(f"Unknown channel type: {channel_type}")
        
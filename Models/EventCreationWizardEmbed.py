from dataclasses import dataclass
from typing import Optional
import discord

@dataclass
class EventCreationWizardEmbed:
    embed: Optional[discord.Embed]
    view: Optional[discord.ui.View] 
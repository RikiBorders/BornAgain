import discord
from discord.ui import Button, View

from Strings.embed_strings import EVENT_CREATION_IMAGE_URL

class Embed:
    def __init__(self):
        self.title = None
        self.description = None
        self.color = None
        self.fields = []

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_color(self, color):
        self.color = color

    def add_field(self, name, value, inline=False):
        field = {
            "name": name,
            "value": value,
            "inline": inline
        }
        self.fields.append(field)

    def build(self):
        pass

class NextPageButton(Button):
    def __init__(self, label, style, custom_id, embeds):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.current_page = 0
        self.embeds = embeds

    async def callback(self, interaction):
        '''
        Desc: Callback function for generating next queue page. Nested due to
              Discordpy design paradigms forcing this design decision.
        '''
        if self.current_page+1 == len(self.embeds):
            self.current_page = 0
        else:
            self.current_page += 1

        await interaction.response.edit_message(embed=self.embeds[self.current_page])


class PreviousPageButton(Button):
    def __init__(self, label, style, custom_id, embeds):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.current_page = 0
        self.embeds = embeds

    async def callback(self, interaction):
        '''
        Desc: Callback function for generating next queue page. Nested due to
              Discordpy design paradigms forcing this design decision.
        '''
        if self.current_page-1 >= 0:
            self.current_page -= 1
        else:
            self.current_page = len(self.embeds)-1

        await interaction.response.edit_message(embed=self.embeds[self.current_page])
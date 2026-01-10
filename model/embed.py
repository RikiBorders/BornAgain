import discord
from discord.ui import Button, View

class Embed:
    def __init__(self, 
                 title: str=None, 
                 description: str=None, 
                 color: str=None, 
                 pages: list["Embed"]=[], 
                 image_url: str=None, 
                 footer: str=None):
        self.title = title
        self.color = color
        self.description = description
        self.image_url = image_url
        self.footer = footer
        self.fields = []

        # Pagination state management
        self.pages = pages

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

    def to_discord_embed(self):
        discord_embed = discord.Embed(
            title=self.title,
            description=self.description,
            color=self.color
        )
        for field in self.fields:
            discord_embed.add_field(
                name=field["name"],
                value=field["value"],
                inline=field["inline"]
            )
        if self.image_url:
            discord_embed.set_image(url=self.image_url)
        if self.footer:
            discord_embed.set_footer(text=self.footer)

        return discord_embed
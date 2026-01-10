from model.embed import Embed
from stringg.help_menu_strings import HELP_MENU_DESCRIPTION
from stringg.embed_strings import WELCOME_EMBED_DESCRIPTIONS
from constant.Constants import BOT_NAME, WELCOME_EMBED_IMAGE_URLS
from random import choice

def build_help_embed():

    embed = Embed(
        title=f"{BOT_NAME} Help Menu",
        description=HELP_MENU_DESCRIPTION,
        color=0x3498db  # Example color
    )
    return embed

def build_welcome_embed(member_count: int):

    embed = Embed(
        title="A New Member has Arrived!",
        description=choice(WELCOME_EMBED_DESCRIPTIONS),
        image_url=choice(WELCOME_EMBED_IMAGE_URLS),
        footer = f"You are the {member_count}th member!", # update this to use 2nd, th, st, etc
        color=0x2ecc71,  # Example color
    )
    return embed
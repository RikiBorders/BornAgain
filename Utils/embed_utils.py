from Models.embed import Embed
from Strings.help_menu_strings import HELP_MENU_DESCRIPTION

def build_help_embed():

    embed = Embed(
        title="BornAgain Help Menu",
        description=HELP_MENU_DESCRIPTION,
        color=0x3498db  # Example color
    )
    return embed
from Bot import Bot

def build_arrakis_event_confirmation_description(title: str, description: str, date:str):
    return (
        f"**Your event is almost ready!**\n\n"
        "Please confirm that the below details are correct\n\n"
        f"**Event Title:** {title}\n"
        f"**Description:** {description}\n"
        f"**Date:** {date}\n"
    )

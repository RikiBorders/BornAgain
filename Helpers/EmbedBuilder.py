import discord
from discord.ui import Button, View

from Models.EventCreationWizardEmbed import EventCreationWizardEmbed

from Strings import EVENT_CREATOR_DESCRIPTION
from Strings import EVENT_CREATOR_TITLE
from Strings import EVENT_CREATION_IMAGE_URL
from Strings import EVENT_CREATION_IMAGE_URL




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

class TriviaAnswerButton(Button):
    def __init__(self, label, style, custom_id, ctx, question, answer_value, correct_answer):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.ctx = ctx
        self.question = question
        self.answer_value = answer_value
        self.correct_answer_value = correct_answer

    async def callback(self, interaction):
        '''
        Desc: Return an indication of whether or not the selected answer was correct or not.
        '''

        if self.answer_value == self.correct_answer_value:
            await interaction.response.edit_message(view=View())
            await interaction.followup.send(f"Correct, The answer was {self.correct_answer_value}!\nNice job {interaction.user.display_name}!")
        else:
            await interaction.response.edit_message(view=View())
            await interaction.followup.send(f"Incorrect! The correct answer was {self.correct_answer_value}. Better luck next time {interaction.user.display_name}")
        
class RadioStationSelectionButton(Button):
    def __init__(self, label, style, custom_id, ctx, station_id, station_name, station_display_name, bot_instance):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.station_display_name = station_display_name
        self.station_id = station_id
        self.station_name = station_name
        self.ctx = ctx
        self.bot_instance = bot_instance

    async def callback(self, interaction):
        '''
        Desc: play the selected radio station
        '''
        await interaction.response.edit_message(view=View())
        await self.bot_instance.verify_voice_channel_status(self.ctx.voice_client, self.ctx.author.voice)
        playing_audio = self.bot_instance.playing_audio(self.ctx.voice_client.is_playing()) if self.ctx.voice_client else False
        radio_station = self.bot_instance.get_radio_station(self.station_name)

        if not playing_audio:
            if not self.bot_instance.in_voice_channel() or self.bot_instance.get_voice_client() != self.ctx.voice_client:
                caller_voice = self.ctx.author.voice
                await caller_voice.channel.connect()
                self.bot_instance.set_voice_client(self.ctx.voice_client)
            
            self.bot_instance.play_audio(
                voice_client=self.ctx.voice_client,
                source=discord.FFmpegPCMAudio(executable=self.bot_instance.get_ffmpeg_path(), source=radio_station.get_playlist()),
                flag='music'
            )

            await interaction.followup.send(f"Now tuning in to {self.station_display_name}. Quack.")
        else:
            await interaction.followup.send(f"It seems like audio is playing. Wait for any currently playing audio to stop playing first! Quack.")

def buildArrakisDataEntryEmbed(title: str, description: str) -> discord.Embed:
    view = View()
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color(0x1253F3)
    )

    return EventCreationWizardEmbed(embed=embed, view=view)

def buildArrakisEventConfirmationEmbed(title: str, event_description: str, date: str) -> discord.Embed:
    view = View()

    description = "lorem ipsum dolorem ipsum lorem ipsum lorem ipsum"

    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color(0xFFFF00)
    )

    return EventCreationWizardEmbed(embed=embed, view=view)
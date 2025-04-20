import discord
from discord.ui import Button, View

from Models.GameSpotArticleEmbed import GameSpotArticleEmbed

class EmbedBuilder:
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



def build_radio_embed():
    '''
    Embed containing radio station selections.
    '''
    title = 'Radio Station Selection'
    description = 'Select an available radio station to tune into!'
    radio_embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color(0x1253F3)
    )
    return radio_embed

def build_meme_embed(meme_data):
    '''
    Embed containing a meme fetched from reddit
    '''
    description = f'Subreddit: {meme_data["subreddit"]}\nAuthor: {meme_data["author"]}'

    meme_embed = discord.Embed(
        title=meme_data['title'],
        description=description,
        color=discord.Color(0x1253F3)
    )
    meme_embed.set_image(url=meme_data['url'])

    return meme_embed


def build_help_embed():
    '''
    Help menu embed
    '''

    description1 = '''All Goose commands are preceded with a period. 
    Below is a list of all Goose commands:\n
    **.play [song name]**: Play *[song name]*. You must be in a voice channel for this command to work.\n
    **.queue**: Display all songs currently in the queue.\n
    **.skip**: Skip the currently playing song.\n
    **.clear**: Remove all songs currently in the queue.\n
    **.remove [song name]**: Remove *[song name]* from the queue. *[song name]* must be typed exactly the same way as it appears in the queue\n
    **.join**: Join the Caller's current voice channel.\n
    **.leave**: If Goose is currently in a voice channel, it will leave.\n
    '''
    description2 = '''
    **.quack**: Quack.\n
    **.meme**: Send a random Reddit meme.\n
    **.trivia**: Send a random trivia question\n
    **.r34 [prompt]**: Send a random NSFW image related to the character name or theme entered in the *[prompt]* field.\n
    '''

    help_embeds = []
    help_embeds.append(discord.Embed(
        title=f'Goose Help Menu. Quack.', 
        description=description1,
        color=discord.Color(0x1253F3)
    ))

    help_embeds.append(discord.Embed(
    title=f'Goose Help Menu Pg.2', 
    description=description2,
    color=discord.Color(0x1253F3)
    ))

    return help_embeds


def build_song_confirmation_embed(song):
    song_info = song.get_data_for_queue()
    description = f'**This song was submitted by {song_info["submitter"]}. Quack**'
    song_embed = discord.Embed(
        title=f'"{song_info["name"]}" has been added to the queue\nDuration: {song_info["length"]}', 
        description=description,
        color=discord.Color(0x1253F3)
    )
    return song_embed


def build_trivia_embed(question_data):
    description = '1. '+question_data['options'][0]

    for index in range(1, len(question_data['options'])):
        description +='\n'+f'{index+1}. '+question_data['options'][index]

    trivia_embed = discord.Embed(
        title=question_data['question'],
        description=description,
        color=discord.Color(0x1253F3)
    )

    return trivia_embed


def build_queue_embeds(bot_instance):
    '''
    Desc: Build embeds for the music queue, and store them on the bot instance.
    '''
    current_song_data = bot_instance.currently_playing_song()
    embed_image = ''
    if current_song_data:
        embed_image = current_song_data.get_thumbnail()
        current_song_data = current_song_data.get_data_for_queue()
        description = f"**Currently playing song: {current_song_data['name']}**\nSubmitted by: {current_song_data['submitter']}\nDuration: {current_song_data['length']}"
    else:
        description = 'Could not fetch current song'
    
    music_queue = bot_instance.get_queue()
    queue_pages = []

    for i in range(len(music_queue)):
        queue_embed = discord.Embed(
            title=f'Current Queue [{i+1}/{len(music_queue)}]', 
            description=description,
            color=discord.Color(0x1253F3)
            )
        if embed_image:
            queue_embed.set_thumbnail(url=embed_image)

        for song in music_queue[i]:
            song_data = song.get_data_for_queue()
            value_info = f"Submitted by: {song_data['submitter']}\n Duration: {song_data['length']}. Position in queue: {song_data['queue_position']}"
            queue_embed.add_field(name=song_data['name'], value=value_info, inline=False)
        
        queue_pages.append(queue_embed)

    bot_instance.set_queue_pages(queue_pages)


def buildGameSpotArticleEmbed(article: dict) -> discord.Embed:
    view = View()

    ArticleOverviewEmbed = discord.Embed(
        title=article.title,
        description=article.deck,
        color=discord.Color(0xff9e00),
    )
    ArticleOverviewEmbed.set_author(name=article.authors)

    # TODO: needs to be limited to <= 4096 characters in length or fewer.
    # We should cut it off with a ..., and provide a link near the bottom.
    ArticleBodyEmbed = discord.Embed(
        title=f"{article.title}...",
        description=article.body,
        color=discord.Color(0xff9e00),
    )
    ArticleEmbeds=[ArticleOverviewEmbed, ArticleBodyEmbed]
    
    prev_page_button = PreviousPageButton(
        label='Prev page', 
        style=discord.ButtonStyle.blurple, 
        custom_id='music_queue_prev_btn',
        embeds=ArticleEmbeds
    )
    next_page_button = NextPageButton(
        label='next page', 
        style=discord.ButtonStyle.blurple, 
        custom_id='music_queue_next_btn',
        embeds=ArticleEmbeds
    )
    view.add_item(prev_page_button)
    view.add_item(next_page_button)

    return GameSpotArticleEmbed(embed=ArticleOverviewEmbed, view=view)   

    
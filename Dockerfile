FROM python

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install "discord.py[voice] @ git+https://github.com/rapptz/discord.py"
# RUN apt-get update && apt-get install -y ffmpeg

CMD [ "python3", "BornAgain.py" ]
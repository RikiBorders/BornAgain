FROM python

WORKDIR /app
COPY . /app


COPY requirements.txt .

# Commented out ffmpeg until we need to play audio
# RUN apt-get update && apt-get install -y ffmpeg
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt && \
    pip install "discord.py[voice] @ git+https://github.com/rapptz/discord.py"

# Copy app after deps are installed so source changes don't bust the pip layer
COPY . .

CMD [ "python3", "BornAgain.py" ]
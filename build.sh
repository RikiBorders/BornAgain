#!/bin/bash
# filepath: /home/rkabord/workspace/discordBot/BornAgain/build.sh

# Build the Docker image
docker build -t test .

# Run the Docker container
docker run test
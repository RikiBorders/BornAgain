#!/usr/bin/env bash
set -euo pipefail
# filepath: /home/rkabord/workspace/discordBot/BornAgain/build.sh

# Enable BuildKit for faster builds and cache mounts
export DOCKER_BUILDKIT=1

IMAGE=bornagain:test

echo "Building ${IMAGE} (BuildKit enabled)"
docker build -t "${IMAGE}" .

CONTAINER="bornagain_run_$RANDOM"
echo "Running ${IMAGE} in container ${CONTAINER}"

# Start container detached with a TTY so we can `docker attach` to it.
docker run --rm -d -it --name "${CONTAINER}" "${IMAGE}"

docker attach "${CONTAINER}"
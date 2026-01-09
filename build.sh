#!/usr/bin/env bash
set -euo pipefail
# filepath: /home/rkabord/workspace/discordBot/BornAgain/build.sh

# Enable BuildKit for faster builds and cache mounts
export DOCKER_BUILDKIT=1

IMAGE=bornagain:latest

echo "Building ${IMAGE} (BuildKit enabled)"
docker build -t "${IMAGE}" .

CONTAINER="bornagain_run_$RANDOM"
echo "Running ${IMAGE} in container ${CONTAINER}"

# Start container detached with a TTY so we can `docker attach` to it.
docker run --rm -d -it --name "${CONTAINER}" "${IMAGE}"

cleanup() {
	echo "Stopping container ${CONTAINER}..."
	docker stop "${CONTAINER}" >/dev/null 2>&1 || true
}

trap cleanup SIGINT SIGTERM EXIT

# Attach to the container so the user can interact. Ctrl+C will be propagated
# to the container; the trap ensures the container is stopped if the script
# receives a signal while attached.
docker attach "${CONTAINER}"

# Wait for the container to exit (if it hasn't already) before finishing.
docker wait "${CONTAINER}" >/dev/null 2>&1 || true
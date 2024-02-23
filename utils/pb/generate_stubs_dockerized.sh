#!/bin/bash
WORKING_DIR=$(dirname "$0")
cd "$WORKING_DIR"

docker build -t pb-stub-generation "$(pwd)"
docker run -v "$(pwd):/pb" pb-stub-generation

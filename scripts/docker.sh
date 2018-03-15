#!/bin/bash

function banner {
    echo "========================================================"
    echo "    $1..."
    echo "========================================================"
}

banner 'Building Docker Container'
docker build -t gmcoinbot .

banner 'Running Docker...'
docker run \
    -it --rm \
    --restart
    --name gmcoinbot \
    --env GMCOINBOT_ENV='PROD' \
    gmcoinbot

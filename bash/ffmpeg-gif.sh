#!/bin/sh

palette="palette.png"

filters="fps=10,scale=500:-1"

ffmpeg -v warning -i $1 -vf "$filters,palettegen=stats_mode=full" -y $palette
ffmpeg -v warning -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse=dither=sierra2" -y $2
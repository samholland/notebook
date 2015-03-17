# Generating gifs with ffmpeg

Based on [the instructions here](http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html), here's a nice setup for generating gifs 

    #!/bin/sh

    # generate a representative palette using ffmpeg palettegen
    # ffmpeg -i [source-video.mov] -vf palettegen palette.png
    # assumes a palette named palette.png

    palette="palette.png"

    # set the filters to establish . Optional scaling: scale=500:-1=flags:lanczos

    filters="fps=10"

    # two pass with options. stats_mode values defaults to full, option diff-will adjust based on differences between frames
    # dithering options include none, floyd_steinberg, sierra2, and sierra2_4a. 
    # the weird option is heckbert. bayer is the standard crosshatching pattern.

    ffmpeg -v warning -i $1 -vf "$filters,palettegen=stats_mode=full" -y $palette
    ffmpeg -v warning -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse=dither=sierra2" -y $2
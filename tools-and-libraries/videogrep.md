# Videogrep

[Videogrep](https://github.com/antiboredom/videogrep)

### Using Videogrep with Youtube

#### Downloading YouTube with subtitles

You can download and convert YouTube video with [youtube-dl](https://github.com/rg3/youtube-dl/blob/master/README.md#readme)

If subtitles already exist:

    youtube-dl --write-sub [video or playlist URL]

If not, auto subtitling:

    youtube-dl --write-auto-sub [video or playlist URL]

Strip the language tag from the .srt filename so that videogrep can find the associated video.

### Using videogrep

Make sure moviepy is up to date.

[Reading material](http://zulko.github.io/blog/2014/06/21/some-more-videogreping-with-python/)

example hypernym: 

    python videogrep.py --input [file] --search 'food' --search-type hyper
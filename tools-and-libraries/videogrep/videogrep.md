# Videogrep

[Videogrep](https://github.com/antiboredom/videogrep)

#### Downloading YouTube with subtitles

You can download and convert YouTube video with [youtube-dl](https://github.com/rg3/youtube-dl/blob/master/README.md#readme)

If subtitles already exist:

    youtube-dl --write-sub [video or playlist URL]

YouTube auto subtitles:

    youtube-dl --write-auto-sub [video or playlist URL]

Dadaesque poetry.

Strip the language tag from the .srt filename so that videogrep can find the associated video.

### Using videogrep

example hypernym: 

    python videogrep.py --input [file] --search 'food' --search-type hyper

### Other video supercut techniques

[Zulko](http://zulko.github.io/blog/2014/06/21/some-more-videogreping-with-python/) outlines a much more precise method on his blog for isolating individual words based on timecode.

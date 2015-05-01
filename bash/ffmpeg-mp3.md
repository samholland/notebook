# converting to mp3

ffmpeg -i <file-to-convert> -vn -ar 44100 -ac 2 -ab 256k -f mp3 <file-to-create>
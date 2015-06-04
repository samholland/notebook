#! /usr/local/bin/python

""" Copied from zulko http://zulko.github.io/blog/2014/06/21/some-more-videogreping-with-python/ """

import re # module for regular expressions
import sys 
from collections import Counter
from moviepy.editor import VideoFileClip, concatenate

# video = sys.argv[0]
# subttls = sys.argv[1]

def convert_time(timestring):
    """ Converts a string into seconds """
    nums = map(float, re.findall(r'\d+', timestring))
    return 3600*nums[0] + 60*nums[1] + nums[2] + nums[3]/1000

with open("coke.srt") as f:
    lines = f.readlines()

times_texts = []
current_times , current_text = None, ""
for line in lines:
    times = re.findall("[0-9]*:[0-9]*:[0-9]*,[0-9]*", line)
    if times != []:
        current_times = map(convert_time, times)
    elif line == '\n':
        times_texts.append((current_times, current_text))
        current_times, current_text = None, ""
    elif current_times is not None:
        current_text = current_text + line.replace("\n"," ")

whole_text = " ".join([text for (time, text) in times_texts]);
all_words = re.findall("\w+", whole_text)
counter = Counter([w.lower() for w in all_words if len(w) > 5])

times, texts = zip(*times_texts)
txt_lengths = map(len, texts) # length of each subtitle block
indices = [sum(txt_lengths[:i]) for i in range(len(texts))]

print (counter.most_common(100))

cuts = [times for (times,text) in times_texts if (re.findall("search string", text) != [])]

video = VideoFileClip("coke.mp4")

def assemble_cuts(cuts, outputfile): 
  """ Concatenate cuts and generate a video file """
  final = concatenate([video.subclip(start, end) for (start,end) in cuts])
  final.to_videofile(outputfile)

assemble_cuts(cuts, "outputvideo.mp4")
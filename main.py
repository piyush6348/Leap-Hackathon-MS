#main.py
import video2Audio as va
import sys
import speechToText as spt
import translate as tr

url = sys.argv[1]
lang_dest = sys.argv[2]
va.vta(url)
response = spt.stt()
captions = response['captions']
keywords = response['keywords']
trans_cap = []
for cap in captions:
    trans_cap.append(tr.translate(cap, lang_dest))



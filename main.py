#main.py
import video2Audio as va
import sys
import speechToText as spt
import translate as tr
import getMeaning as gm

results = {}
trans_cap = []
meaning = []
# url = sys.argv[1]
# lang_dest = sys.argv[2]

url = 'https://youtu.be/VJCXwxvLNkY'
lang_dest = 'ar'

va.vta(url)
response = spt.getText()
captions = response['captions']
keywords = response['keywords']
results['captions'] = ' '.join(captions)
results['keywords'] = keywords
for cap in captions:
    trans_cap.append(tr.translate(cap, lang_dest))
results['translation'] = trans_cap
# keywords = [['way', 'great work'], ['matters', 'heart', 'Love'], ['head', 'brick', 'faith', "life's", 'thing'], ['gut destiny life', 'dots', 'future'], ['dots', 'confidence', 'road', 'worn path', 'Karma', 'heart'], ['difference', 'time', 'life'], ["people's thinking", 'inner voice', 'noise', 'opinions', 'results', 'dogma'], ['courage', 'heart', 'intuition']]
for k in keywords:
    meaning.append(gm.get_meaning(k))
results['meaning'] = meaning
results['summary'] = ''

print(results)

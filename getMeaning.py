import requests
import json
import os
    
def get_meaning(words=[]):
    meaning = []
    for i,word in enumerate(words):
        url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search='+word+'&format=json&callback=?'
        response = requests.get(url)
        str = response._content.decode('utf-8')[5:-1]
        resp = json.loads(str)
        meaning.append(resp[2][0])
    return meaning

print (get_meaning(['Earth', 'Temple']))

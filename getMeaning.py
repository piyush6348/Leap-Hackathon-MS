import requests
import json
import os
    
def get_meaning(words=[]):
    meaning = []
    for i,word in enumerate(words):
        url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search='+word+'&format=json&callback=?'
        response = requests.get(url)
        s = response._content.decode('utf-8')[5:-1]
        resp = json.loads(s)
        if resp and len(resp)>1 and resp[2]:
            meaning.append(resp[2][0])
    return meaning

# print (get_meaning(['way', 'great work']))

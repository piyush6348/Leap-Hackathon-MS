import requests
import json
import os
import sys

def getKeywords(text=None):
    if text is None:
        print("No valid text")
        sys.exit(1)

    keywords = list()

    import http.client, urllib.request, urllib.parse, urllib.error, base64

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '3e433c7dbd734d87a82d9746ea82587d'
    }

    params = urllib.parse.urlencode({ })

    body = {
      "documents": [
            {
                "language": "en",
                "id": "1",
                "text": text
            }
        ]
    }

    try:
        # conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(body), headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data)
        # print(data)
        keywords = data['documents'][0]['keyPhrases']
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return keywords


def getText():

    # get token
    header = {
        'Content-type':'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Ocp-Apim-Subscription-Key':'bd9852f25e2b4ebca00a832fef77abee'
        }
    response = requests.post('https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken', headers=header)
    # print(type(response))
    # print(response.text)

    SpeechServiceURI ='https://westus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-us&format=detailed'
    authorization = 'Bearer ' + response.text
    recoRequestHeader = {
        'Authorization' : authorization,
        # 'Transfer-Encoding' : 'chunked',
        'Content-type' : 'audio/wav; codec=audio/pcm; samplerate=16000'
        }

    # base_dir = 'C:\\Users\\Administrator\\Desktop\\Hackathon project\\out\\'
    base_dir = os.getcwd()
    base_dir = os.path.join(base_dir, "out")
    files = os.listdir(base_dir)
    output = {
        'captions': [],
        'keywords': []
        }
    for x in files:
        audioBytes = open(os.path.join(base_dir,x), 'rb').read()

        textGenerated = requests.post(SpeechServiceURI, headers=recoRequestHeader, data=audioBytes)
        # print(textGenerated.__dict__.keys())
        data = json.loads(textGenerated.text)
        
        text = data.get('NBest', None)
        if text:
            text = text[0]['Display']
        else:
            continue

        # print(text)
        keywords = getKeywords(text)
        # print(keywords)
        output['captions'].append(text)
        output['keywords'].append(keywords)
    return output

# getText()

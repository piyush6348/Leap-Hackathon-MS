import requests
import json
import os

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

# with open(r"C:\Users\utchauha\Downloads\LeapHackathon\eng_f4.wav", 'rb') as f:
#    audioBytes = f.read()

base_dir = 'C:\\Users\\Administrator\\Desktop\\Hackathon project\\out\\'
files = os.listdir(base_dir)
for x in files:
    audioBytes = open(base_dir+x, 'rb').read()

    textGenerated = requests.post(SpeechServiceURI, headers=recoRequestHeader, data=audioBytes)
    # print(textGenerated.__dict__.keys())
    data = json.loads(textGenerated.text)
    # text = textGenerated.__dict__['_content']['NBest']
    # print(data)
    # for k,d in data['NBest'][0].items():
            # print("key: ", k, " data: ", d)
    
    text = data.get('NBest', None)
    if text:
        text = text[0]['Display']
    else:
        continue

    print(text)

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

    print(keywords)

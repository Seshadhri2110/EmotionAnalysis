import requests
import json

def emotion_detector(text_to_analyse,header,url):
 input_json = { "raw_document": { "text": text_to_analyse } }
 response = requests.post(url, json=input_json, headers=header, timeout=30)
 status_code = response.status_code
 emotions = {}
 if status_code == 200:
 formatted_response = json.loads(response.text)
 emotions = formatted_response['emotionPredictions'][0]['emotion']
 dominant_emotion = max(emotions.items(), key=lambda x: x[1])
 emotions['dominant_emotion'] = dominant_emotion[0]
 elif status_code == 400:
 emotions['anger'] = None
 emotions['disgust'] = None
 emotions['fear'] = None
 emotions['joy'] = None
 emotions['sadness'] = None
 emotions['dominant_emotion'] = None 
 return response, status_code,emotions

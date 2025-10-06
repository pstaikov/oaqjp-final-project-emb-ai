import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = input_text, headers=headers)
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None}
    formatted_resp = json.loads(response.text)
    em_scores = formatted_resp['emotionPredictions'][0]['emotion'] 
    dominant_emotion = max(em_scores, key=em_scores.get)
    em_scores['dominant_emotion'] = dominant_emotion
    return em_scores
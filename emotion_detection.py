import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the emotion detection service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Construct the request payload
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the emotion detection API
    response = requests.post(url, json = myobj, headers = header)

    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extract the required set of emotions
    emotion = formatted_response['emotionPredictions'][0]['emotion']

    # Extract the set of emotions one after the other using string method
    anger_score = emotion['anger']
    disgust_score = emotion['disgust']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    sadness_score = emotion['sadness']

    # The logic to get the dominant emotion (highest score)
    dominant_emotion = max(emotion, key=emotion.get)
    
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}

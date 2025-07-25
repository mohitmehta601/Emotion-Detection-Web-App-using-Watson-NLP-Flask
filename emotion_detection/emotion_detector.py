import requests

def emotion_predictor(text):
    if not text:
        return {"error": "Input text is empty."}

    url = "https://watson-nlp-api-url.com/analyze"
    params = {
        "text": text,
        "features": "emotion"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {"error": f"API error. Status code: {response.status_code}"}

    emotions = response.json().get('emotion', {}).get('document', {}).get('emotion', {})
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "emotion": dominant_emotion,
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0)
    }

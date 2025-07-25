from flask import Flask, request, jsonify
from emotion_detection import emotion_predictor

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def get_emotion():
    text = request.args.get("textToAnalyze", "")
    result = emotion_predictor(text)

    if "error" in result:
        return result["error"], 400

    response = f"For the given statement, the system predicts the emotion as {result['emotion']} with confidence scores: {result}"
    return response

if __name__ == "__main__":
    app.run(debug=True)

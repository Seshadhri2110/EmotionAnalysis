from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():

    text_to_analyse = request.args.get('textToAnalyze')

    # Check whether text was provided
    if not text_to_analyse:
        return "Invalid text! Please try again", 400

    emotion_result = emotion_detector(text_to_analyse)

    # Check whether emotion detection was successful
    if emotion_result['dominant_emotion'] is None:
        return "Invalid text! Please try again", 400

    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy}, "
        f"'sadness': {sadness}, "
        f"'dominant_emotion': {dominant_emotion}"
    )

    return response, 200


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

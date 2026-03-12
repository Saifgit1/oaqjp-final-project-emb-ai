from flask import Flask , request, render_template, jsonify
import json
from EmotionDetection import emotion_detector
app =Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_sent():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
     
     
    return (
    f"'anger': {response['anger']}\n"
    f"'disgust': {response['disgust']}\n"
    f"'fear': {response['fear']}\n"
    f"'joy': {response['joy']}\n"
    f"'sadness': {response['sadness']}\n"
    f"'dominant_emotion': {response['dominant_emotion']}"
)


    

if __name__ == '__main__':
    app.run(debug=True)


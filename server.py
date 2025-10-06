from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def sent_text():
    text_to_analyze = request.args.get('textToAnalyze')
    em_scores = emotion_detector(text_to_analyze)
    dominant_emotion = em_scores["dominant_emotion"]
    if not dominant_emotion:
        return "Ivalid text! Please try again!"
    em_scores.pop("dominant_emotion", None)
    return "For the given statement, the sistem response is " + \
        f"'anger': {em_scores['anger']}, " + \
        f"'disgust': {em_scores['disgust']}, " + \
        f"'fear': {em_scores['fear']}, " + \
        f"'joy': {em_scores['joy']}, and " + \
        f"'sadness': {em_scores['sadness']}. " + \
        f"The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

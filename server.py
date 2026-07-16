"""
Import Flask, render_template, request from flask into the server file.
Import emotion_detector from EmotionDetector folder inside the emotion_detection file.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    The decorator shows where the route of the function operates once it's called and,
    below are the actions carried out by the function once called upon.
    """
    # Retrieve the text to analyze from the request argument
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the set of emotions one after the other using string method
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Handle invalid/blank input
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    # Return a formatted string with the emotion attached to each statement and the dominant
    return (
    f"For the given statement, the system response is 'anger': {anger_score}, "
    f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, "
    f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}"
    )

@app.route("/")
def render_index_page():
    """
    This function renders the html page 
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import *  
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
@app.route('/') 
def home():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak(query)
    except Exception as e:
        query = "Say that again please..."
        speak(query)
    return render_template('message.html',query=query)  
  
if __name__ =='__main__':  
    app.run(debug = True)  
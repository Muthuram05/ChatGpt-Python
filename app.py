from flask import *  
import speech_recognition as sr


app = Flask(__name__)  
 
@app.route('/') 
def home():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please...")
            print("None")
        return render_template('message.html',query=query)  
  
if __name__ =='__main__':  
    app.run(debug = True)  
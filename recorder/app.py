import os
import uuid
from flask import Flask, flash, request, redirect
import speech_recognition as sr


UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_name = str(uuid.uuid4()) + ".mp3"
    output_file = 'user_recording.wav'
    file.save(output_file)
    r = sr.Recognizer()
    with sr.AudioFile(output_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-IN', show_all=True)
    print(text)
    return '<h1>Success</h1>'


if __name__ == '__main__':
    app.run()

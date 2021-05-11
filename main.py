#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
from audio import BabyAudio
import time
import threading
import os
import pyaudio

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.


# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/audio')
def audio():
    # start Recording
    return Response(BabyAudio.sound())

@app.route('/stop_audio')
def stop_audio():
    # stop audio
    BabyAudio.stopSound()

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=False)
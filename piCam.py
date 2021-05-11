from time import sleep
from io import BytesIO
from picamera import PiCamera
import time


class VideoCamera(object):
    def __init__(self):
        self.camera = PiCamera()
        # self.camera.resolution = (640, 480)
        self.stream = BytesIO()
        time.sleep(2.0)
        self.camera.start_recording(self.stream, format='h264', quality=25)

    def __del__(self):
        self.camera.stop_recording()


    def get_frame(self):
        return self.stream.getvalue()

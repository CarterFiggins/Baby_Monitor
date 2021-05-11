import pyaudio


class PiAudio(object):
  def __init__(self ):
    self.format = pyaudio.paInt16
    self.sampleRate = 44100
    self.bitsPerSample = 16
    self.channels = 1
    self.piAudio = pyaudio.PyAudio()
    self.rate = 44100
    self.chunk = 10000
    self.input_device_index = 2
    self.soundOn = False

  # start Recording
  def sound(self):

    wav_header = genHeader(self.sampleRate, self.bitsPerSample, self.channels)

    stream = piAudio.open(format=self.format, channels=self.channels,
                    rate=self.rate, input=True,input_device_index=self.input_device_index,
                    frames_per_buffer=self.chunk)
    print("recording...")
    #frames = []
    first_run = True
    self.soundOn = True
    while self.soundOn:
        if first_run:
            data = wav_header + stream.read(self.chunk)
            first_run = False
        else:
            data = stream.read(self.chunk, exception_on_overflow=False)
        yield(data)

  def stopSound(self):
    self.soundOn = False

  def genHeader(sampleRate, bitsPerSample, channels):
    datasize = 2000*10**6
    o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
    o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
    o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
    o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
    o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    return o
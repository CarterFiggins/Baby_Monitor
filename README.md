## Video

```
sudo apt-get install libatlas-base-dev

sudo apt-get install libjasper-dev

sudo apt-get install libqtgui4

sudo apt-get install libqt4-test

sudo apt-get install libhdf5-dev

sudo pip3 install Flask

sudo pip3 install numpy

sudo pip3 install opencv-contrib-python

sudo pip3 install imutils

sudo pip3 install opencv-python
```

## Audio

`sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev`

`sudo pip3 install pyaudio`

## instructions

To start manually

python main.py

Systemd

path to get there on rpi

/etc/systemd/system

add service to boot up server

TODO: explain the babyCam.service

```
[Unit]
Description=Baby Camera web application

[Service]
User=pi
Type=idle
WorkingDirectory=/home/pi/babyCam
Restart=always
ExecStart=/usr/bin/python3 /home/pi/babyCam/main.py

[Install]
WantedBy=multi-user.target
```

`service <service_file> start`/`stop`/`service`

`sudo systemctl daemon-reload`

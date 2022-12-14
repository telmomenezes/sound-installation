from random import randrange
import serial
import time

import vlc

files = ['audio/L10 Demo Voc Reverb 1.aif',
         'audio/Grand Piano Dirty Stabs E Minor 90 bpm.wav',
         'audio/Electric Guitar Funky Wah G# Minor 115 bpm.wav',
         'audio/Organic Bells TL Amin 115 bpm.wav']

def play(audio_dir):
    with serial.Serial('/dev/cu.usbmodem11301', 9800, timeout=1) as ser:
        ser.write(b'A')
        time.sleep(1)
        while True:
            # for speaker in [b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'N', b'O', b'P']:
            # for speaker, file in zip([b'A', b'B', b'C', b'D'], files):
            pos = randrange(4)
            speaker = [b'A', b'B', b'C', b'D'][pos]
            file = files[pos]
            ser.write(speaker)
            print(speaker)
            # p = vlc.MediaPlayer('audio/in_c.aif')
            p = vlc.MediaPlayer(file)
            p.play()
            # print(p.get_length())
            time.sleep(5)
            p.stop()


def list_ports():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

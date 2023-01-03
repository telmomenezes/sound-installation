import os
import serial
import time
import random

import serial.tools.list_ports
import vlc

files = ['audio/L10 Demo Voc Reverb 1.aif',
         'audio/Grand Piano Dirty Stabs E Minor 90 bpm.wav',
         'audio/Electric Guitar Funky Wah G# Minor 115 bpm.wav',
         'audio/Organic Bells TL Amin 115 bpm.wav']

folders = ['Anati_Son', 'Denis_Son', 'Moritz_Son', 'Nikola_Son', 'Petra_Son', 'Sanja_Son', 'Coline_Son', 'Frank_Son',
           'Nazan_Son', 'Pascal_Son', 'Raluca_Son', 'Sebas_Son', 'Telmo_Son']


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    serial_ports = []
    for port, desc, hwid in sorted(ports):
        print('{}: {} [{}]'.format(port, desc, hwid))
        serial_ports.append(port)
    return serial_ports


def find_arduino_port():
    ports = list_serial_ports()
    arduino_port = None
    for port in ports:
        if 'usbmodem' in port:
            print('arduino port found: {}'.format(port))
            return port
    print('no arduino port found')
    return None


def choose_random_file(folder):
    return '{}/{}'.format(folder, random.choice(os.listdir(folder)))


def loop(ser):
    if ser:
        ser.write(b'A')
    time.sleep(1)
    while True:
        pos = random.randrange(13)
        file = choose_random_file('sounds/{}'.format(folders[pos]))
        print(file)
        speaker = [b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J', b'K', b'L', b'M'][pos]
        if ser:
            ser.write(speaker)
        print(speaker)
        p = vlc.MediaPlayer(file)
        p.play()
        time.sleep(1)
        length = p.get_length()
        print('length: {} ms'.format(length))
        time.sleep(length / 1000.0)
        p.stop()


def play(audio_dir):
    arduino_port = find_arduino_port()
    # with serial.Serial('/dev/cu.usbmodem11301', 9800, timeout=1) as ser:
    if arduino_port:
        with serial.Serial(arduino_port, 9800, timeout=1) as ser:
            loop(ser)
    else:
        print('WARNING: running without arduino')
        loop(None)

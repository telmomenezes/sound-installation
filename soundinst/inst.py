import serial
import time


def play(audio_dir):
    with serial.Serial('/dev/cu.usbmodem11301', 9800, timeout=1) as ser:
        while True:
            for speaker in [b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H',
                            b'I', b'J', b'K', b'L', b'M', b'N', b'O', b'P']:
                time.sleep(0.5)
                ser.write(speaker)


def list_ports():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

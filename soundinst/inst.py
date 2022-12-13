import serial
import time


def play(audio_dir):
    with serial.Serial('/dev/cu.usbmodem11301', 9800, timeout=1) as ser:
        while True:
            time.sleep(0.5)
            ser.write(b'H')
            time.sleep(0.5)
            ser.write(b'L')


def list_ports():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

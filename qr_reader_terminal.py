import cv2, time, signal
from pyzbar import pyzbar

def signal_handler(signal, frame):
    print("\nClosing ...\n")
    exit(0)

def read_qr(frame):
    if frame is not None:
        barcodes = pyzbar.decode(frame)

        for qr in barcodes:
            qr = qr.data.decode('utf-8')
            return qr

def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    while ret:

        ret, frame = camera.read()
        qr = read_qr(frame)

        if qr is not None:
            print(f"qr code detected: {qr}")

    camera.release()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from hashalgo import hashfun
import pyqrcode
import time

def qrmaker(aadharnum):

    bsfnum=hashfun.bsfenc(aadharnum)

    qr = pyqrcode.create(bsfnum)
    savestring =bsfnum
    qr.png('C:/Users/Aryan-PC/PycharmProjects/testproject/qrcollector/'+savestring+'.png',scale=6)


def qrscanner():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 640)
    cap.set(4, 480)
    l = []

    runner = True
    while runner:

        success, img = cap.read()
        for barcode in decode(img):
            l.append(barcode.data.decode('utf-8'))
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            time.sleep(2)
            break
        cv2.imshow('QR Scanner-Apollo Systems', img)
        cv2.waitKey(1)
        if len(l) == 1:
            break
        if cv2.getWindowProperty('QR Scanner-Apollo Systems', cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()


    try:
        bsfnum=l[0]
    except :
        print("Closed scanner window")
    aadharnumber = hashfun.bsfdec(bsfnum)
    return hashfun.hashalgorithm(aadharnumber)





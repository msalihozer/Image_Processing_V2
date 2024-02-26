import datetime
import cv2
import sys
import time
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import gmtime, strftime
import pyrebase
sure = input("Kaç saniye de görüntü alınsın =")
sure = int(sure)
# Pc Kamerası
videom = cv2.VideoCapture()
cred = credentials.Certificate("xxx.json")
# Admin için :
firebase_admin.initialize_app(cred, {
   "databaseURL": "https://sistem-xxxx-default-rtdb.firebaseio.com/"
})
ref = db.reference("KAMERA-1")
ref2 = db.reference("/" + "KAMERA-2")
kk = 0
ff = 0
while True:
    ret, frame1 = videom.read() #Alınan framlerin okunması
    time.sleep(sure)
    ret, frame2 = videom.read()

    roi1 = frame1[0:200, 100:400] #Alınan görüntünün kordinatlarının belirlenmesi y,y x,x
    roi2 = frame2[0:200, 100:400]

    #Gri tonlaması yapılarak ilk alınan frame ile son alınan frame arasında fark bulma
    fark1 = cv2.absdiff(roi1, roi2)
    gri1 = cv2.cvtColor(fark1, cv2.COLOR_BGR2GRAY)
    blur1 = cv2.GaussianBlur(gri1, (5, 5), 0)
    _, esik1 = cv2.threshold(blur1, 20, 255, cv2.THRESH_BINARY)
    genis1 = cv2.dilate(esik1, None, iterations=3)
    kontur1, _ = cv2.findContours(genis1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Hareket kontrol
    if kontur1:
        for k in kontur1:
            (x, y, w, h) = cv2.boundingRect(k)
            if cv2.contourArea(k):
                cv2.rectangle(frame1, (x, y), (w + x, h + y), (0, 0, 255), 2)
    else:
        cv2.putText(roi1, "DURUM: {}".format('HAREKET YOK'), (10, 10), cv2.FONT_HERSHEY_TRIPLEX,
                    0.5, (255, 0, 0), 1)
        f = strftime("%a, %d %b %Y %H:%M:%S")
        print("cam1 Hareket Yok!" + " " + "Tarih: "+f)
        ref.update({kk: {"uyari cam 1": f}})
        kk = kk + 1
        if kk == 15:
            kk = 0

        continue  

    #Kamera 2
    ret, frame3 = videom.read()
    time.sleep(sure)
    ret, frame4 = videom.read()
    roi3 = frame3[100:500, 100:400]
    roi4 = frame4[100:500, 100:400]

    fark = cv2.absdiff(roi3, roi4)
    gri = cv2.cvtColor(fark, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (5, 5), 0)
    _, esik = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    genis = cv2.dilate(esik, None, iterations=3)
    kontur, _ = cv2.findContours(genis, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if kontur:
        for a in kontur:
            (x, y, w, h) = cv2.boundingRect(a)
            if cv2.contourArea(a):
                cv2.rectangle(frame3, (x, y), (w + x, h + y), (0, 0, 255), 2)
    else:
            cv2.putText(roi3, "DURUM: {}".format('HAREKET YOK'), (10, 10), cv2.FONT_HERSHEY_TRIPLEX,
                        0.5, (0, 0, 255), 1)
            tt = strftime("%a, %d %b %Y %H:%M:%S")

            print("cam2 Hareket Yok!" + " " + "Tarih: " + tt)
            ref2.update({
                ff: {"uyari cam 2": tt}})
            ff = ff + 1
            if ff == 15:
                ff = 0
            continue

    #os.system('py epost2.py') e-posta gönderimi kamera 2 için

    cv2.imshow('cam1', roi1)
    roi1 = roi2
    ret, roi2 = videom.read()
    cv2.imshow('cam2', roi3)
    roi3 = roi4
    ret, roi4 = videom.read()

    #ESC ÇIKIŞ VE FRAMELER İÇİN SÜRE AYARI
    if cv2.waitKey(10) & 0xFF == 27:
        break
videom.release()
cv2.destroyAllWindows()
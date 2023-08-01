import sys
import cv2
import numpy as np
import time
import keyboard
from math import sqrt
from PIL import Image
from web import *
import picamera
from picamera.array import PiRGBArray

sys.dont_write_bytecode = True

def testFunction():
    lowerBound = np.array([33, 80, 40])
    upperBound = np.array([102, 255, 255])

    with picamera.PiCamera() as cam:
        cam.resolution = (340, 220)
        rawCapture = PiRGBArray(cam, size=(340, 220))
        time.sleep(0.1) # Allow the camera to warm up

        kernelOpen = np.ones((5, 5))
        kernelClose = np.ones((20, 20))

        x_coor = []
        y_coor = []
        cords = []

        img1 = np.zeros((512, 512, 3), np.uint8)

        for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            img = frame.array
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(imgHSV, lowerBound, upperBound)
            maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
            maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

            maskFinal = maskClose
            conts, _ = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            for contour in conts:
                x, y, _, _ = cv2.boundingRect(contour)
                x_coor.append(x)
                y_coor.append(y)
                cords.append((x, y))

                if len(cords) >= 2:
                    hello = cv2.line(img1, cords[-1], cords[-2], (0, 255, 255), 2)

            if keyboard.is_pressed('s'):
                cv2.imwrite("img.jpg", hello)
                cv2.destroyAllWindows()
                break

            for i in range(len(conts)):
                x, y, w, h = cv2.boundingRect(conts[i])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow("cam", img)

            rawCapture.truncate(0) # Clear the stream for the next frame

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    image = cv2.imread("img.jpg")
    image2 = cv2.imread("img2.jpg")
    original = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([22, 93, 0], dtype="uint8")
    upper = np.array([45, 255, 255], dtype="uint8")
    mask = cv2.inRange(image, lower, upper)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    print("Number of contours:" + str(len(cnts)))
    for c in cnts:
        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image2, (x, y), (x + w, y + h), (255, 0, 0), 3)
    crop_img = image2[y:y + h, x:x + w]
    crop_img = cv2.resize(crop_img, (340, 340))
    cv2.imwrite("1.jpg", crop_img)
    web_part()

while True:
    if keyboard.is_pressed('q'):
        with picamera.PiCamera() as videoCaptureObject:
            videoCaptureObject.resolution = (340, 220)
            rawCapture = PiRGBArray(videoCaptureObject, size=(340, 220))
            time.sleep(2)

            for frame in videoCaptureObject.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                frame = frame.array
                frame = cv2.resize(frame, (340, 220))
                cv2.imwrite("img2.jpg", frame)
                break

        testFunction()

    if keyboard.is_pressed('e'):
        sys.exit()

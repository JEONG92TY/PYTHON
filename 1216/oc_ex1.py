import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture("./1216/ex1.jpg")

if not cap.isOpened() :
    print("not exist")
    exit()

while True :
    ret, frame = cap.read()
    if not ret :
        break

    frame = cv2.resize(frame, (640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([35,40,40])
    upper = np.array([150,255,255])
    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask_contours = cv2.drawContours(frame, contours, -1, (0,255,0), 2)
    #for con in contours :
    #    ares =  cv2.contourArea(con)
    #    cv2.drawContours(frame, [con], -1, (0,255,0), 2)

    for cnt in contours :
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('oooo', frame)
    print(len(contours))
    cv2.waitKey(0)

    #if cv2.waitKey(1) == ord('q') :
    #    break
    #cap.release()
    #cv2.destroyAllWindows
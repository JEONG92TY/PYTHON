import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
image = cv2.imread("./1216/test.jpg")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([0, 120, 70])
upper = np.array([10, 255, 255])

mask = cv2.inRange(hsv_image, lower, upper)

result = cv2.bitwise_and(image, image, mask=mask)

plt.subplot(1,3,1)
plt.title("original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1,3,2)
plt.title("mask")
plt.imshow(mask, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("result")
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
'''

'''
cap = cv2.VideoCapture("./1213/video.mp4")

if not cap.isOpened() :
    print("not exist")
    exit()

while True :
    ret, frame = cap.read()
    if not ret :
        break

    frame = cv2.resize(frame, (640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0,20,70])
    upper = np.array([20,255,255])

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for con in contours :
        ares =  cv2.contourArea(con)
        cv2.drawContours(frame, [con], -1, (0,255,0), 2)

    cv2.imshow('skin', frame)
    cv2.imshow('mask', mask)

    cv2.waitKey(0)

    #if cv2.waitKey(1) == ord('q') :
    #    break
    #cap.release()
    #cv2.destroyAllWindows
'''

# 얼굴 가져오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 눈 가져오기
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture("./1216/test.jpg")

if not cap.isOpened() :
    print("not exist")
    exit()

while True :
    ret, frame = cap.read()
    if not ret :
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 얼굴 그리기
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for(x,y,w,h) in faces :
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        # 눈 그리기
        eyes = eye_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=10, minSize=(15,15))

        for ( ex, ey, ew, eh) in eyes :
            cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
        
        cv2.imshow('eye', frame)

    #cv2.imshow('face', frame)
    cv2.waitKey(0)

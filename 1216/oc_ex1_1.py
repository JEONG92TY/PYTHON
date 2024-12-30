import cv2
import numpy as np

image = cv2.imread("./1216/apple.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([40,50,50])
upper = np.array([85,255,255])
mask = cv2.inRange(hsv, lower, upper)

mask = cv2.erode(mask, None, iterations=3)
mask = cv2.dilate(mask, None, iterations=3)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(f"contour 개수 : {len(contours)}")

#mask_contours = cv2.drawContours(image, contours, -1, (0,255,0), 2)
#cv2.imshow("c", mask_contours)

for cnt in contours :
    area = cv2.contourArea(cnt)
    if area > 3000 :
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,0), 1)

cv2.imshow("b", image)

cv2.waitKey(0)
import cv2
import numpy as np

image = cv2.imread("./1212/down.jpg")


(h,w) = image.shape[:2]
center = (w//2, h//2)
'''
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w,h))

cv2.imshow("image", rotated)
cv2.waitKey(0)
'''

matrix = np.float32([[1,0,100], [0,1,50]])
move = cv2.warpAffine(image, matrix, (w,h))

cv2.imshow("image", move)
cv2.waitKey(0)
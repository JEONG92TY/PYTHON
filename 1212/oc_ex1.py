import cv2
import numpy as np

image = cv2.imread("./1212/down.jpg")
image_gratscale = cv2.imread("./1212/down.jpg", cv2.IMREAD_GRAYSCALE)
scale = 0.5
resized_image = cv2.resize(image, None, fx=scale, fy=scale)
(h,w) = image.shape[:2]
center = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, matrix, (w,h))

cv2.imshow("Ori", image)
cv2.imshow("Gra", image_gratscale)
cv2.imshow("Res", resized_image)
cv2.imshow("Rot", rotated)

cv2.waitKey(0)

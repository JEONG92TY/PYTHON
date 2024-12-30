import cv2
from ultralytics import YOLO

'''
model = YOLO('yolov8n.pt')
image = cv2.imread('./1216/test3.jpg')

results = model.predict(source=image, save=False, save_txt=False, conf=0.5)
frame = results[0].plot()

cv2.imshow('YOLO', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import pytesseract

pytesseract.pytesseract.tesseract_cmd = ''"C:/Program Files/Tesseract-OCR/tesseract.exe"

image = cv2.imread("./1216/bill.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray_image, 40, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(binary_image, lang="kor")
print(text)
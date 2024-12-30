import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture("./1213/video.mp4")

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("./1213/output.avi", codec, 20.0, (640,480))

plt.ion()

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret :
        print("프레임 읽기 실패")
        break
    
    #out.wirte(frame)
    #cv2.imshow("Video", frame)
    original = frame.copy()

    gaussian = cv2.GaussianBlur(frame, (9,9), 0)

    plt.subplot(2,2,1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("원본")
    plt.axis('off')

    plt.subplot(2,2,2)
    plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
    plt.title("가우시안")
    plt.axis('off')

    plt.pause(0.001)
    plt.clf()
    
    key = cv2.waitKey(1)
    if key == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()
plt.close()
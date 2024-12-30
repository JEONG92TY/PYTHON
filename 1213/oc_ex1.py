import matplotlib.pyplot as plt
import numpy as np
import cv2

ori = cv2.VideoCapture("./1213/video.mp4")

plt.ion()
#그리는법 2
fig, axes = plt.subplots(2, 2, figsize=(5,5))

while ori.isOpened():
    ret, frame = ori.read()
    if not ret :
        break

    #--------컨투어
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #그레이스케일로 변환

    # #이진화처리
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # #컨투어 감지
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # #컨투어 원본에 그리기
    results_avi= frame.copy()
    cv2.drawContours(results_avi, contours, -1, (0, 255, 0), 2)

    # 샤프닝 커널
    kernel = np.array([[0, -1, 0],
                    [-1, 9, -1],
                    [0, -1, 0] ])
    # 필터 적용
    sharped =  cv2.filter2D(results_avi, -1, kernel)

    axes[0,0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title("original")
    axes[0,0].axis('off')

    axes[0,1].imshow(cv2.cvtColor(results_avi, cv2.COLOR_BGR2RGB))
    axes[0,1].set_title("contour")
    axes[0,1].axis('off')

    axes[1,0].imshow(cv2.cvtColor(sharped, cv2.COLOR_BGR2RGB))
    axes[1,0].set_title("sharp")
    axes[1,0].axis('off')

    plt.pause(0.001)
    plt.clf()

    key = cv2.waitKey(1)  # 키 입력 대기 (1ms)
    if key == ord('q'):  # 'q' 키가 입력되었는지 확인
        break

ori.release()
cv2.destroyAllWindows()
plt.ioff()
#plt.close()

'''
    plt.subplot(2,2,1)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title("original")
    plt.axis('off')

    plt.subplot(2,2,2)
    plt.imshow(cv2.cvtColor(results_avi, cv2.COLOR_BGR2RGB))
    plt.title("contour")
    plt.axis('off')

    plt.subplot(2,2,3)
    plt.imshow(cv2.cvtColor(sharped, cv2.COLOR_BGR2RGB))
    plt.title("sharp")
    plt.axis('off')
'''
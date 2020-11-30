import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.load('myHogDector.bin')
cap = cv2.VideoCapture(0)
while True:
    # 读摄像头
    ok, img = cap.read()
    # 或用某图片
    # img = cv2.imread(r'D:\Programs\MyResearch\HOG_SVM\INRIAPerson2\Test\pos\crop_000006.png')
    rects, wei = hog.detectMultiScale(img, winStride=(4, 4), padding=(8, 8), scale=1.05)
    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('a', img)
    if cv2.waitKey(1) & 0xff == 27:  # esc键退出
        break
cv2.destroyAllWindows()
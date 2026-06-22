import cv2
import numpy as np

def callback():
    pass

# 创建窗口
cv2.namedWindow("trackbar",cv2.WINDOW_NORMAL)

# 设置窗口大小
cv2.resizeWindow("trackbar",640,480)

# 创建滑动条
cv2.createTrackbar("R","trackbar",0,255,callback)
cv2.createTrackbar("G","trackbar",0,255,callback)
cv2.createTrackbar("B","trackbar",0,255,callback)

img = np.zeros((480,640,3),dtype=np.uint8)

while True:
    # 获取滑动条的值
    r = cv2.getTrackbarPos("R","trackbar")
    g = cv2.getTrackbarPos("G","trackbar")
    b = cv2.getTrackbarPos("B","trackbar")

    # 创建背景图像
    img = np.zeros((480,640,3),dtype=np.uint8)
    img[:] = (b,g,r)

    # 显示图像
    cv2.imshow("trackbar",img)

    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break


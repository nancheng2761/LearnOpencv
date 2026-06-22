import cv2
import numpy as np

# 鼠标回调函数
def mouse_Callback(event,x,y,flags,userdata):
    print("event:",event,x,y,flags,userdata)

# 创建窗口
cv2.namedWindow("mouse",cv2.WINDOW_NORMAL)
cv2.resizeWindow("mouse",640,480)

# 设置鼠标回调函数
cv2.setMouseCallback("mouse", mouse_Callback,"123")

# 显示窗口和背景
while True:
    img = np.zeros((480,640,3),dtype=np.uint8)
    cv2.imshow("mouse",img)
    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
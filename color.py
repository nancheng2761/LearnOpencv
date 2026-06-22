import cv2
import numpy as np

def callback(x):
    print

# 创建窗口
cv2.namedWindow("color",cv2.WINDOW_NORMAL)

img_path = r"C:\BaiduSyncdisk\闲杂物品\图片\5b9839a12a0cdf4477.jpg"
img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)

colorspaces = [cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,
              cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HSV_FULL,
              cv2.COLOR_BGR2YUV]

# 创建滑动条
cv2.createTrackbar("curcolor","color",0,len(colorspaces)-1,callback)
while True:
    # 获取滑动条的值
    index = cv2.getTrackbarPos("curcolor","color")

    # 转换颜色空间api
    cv_img = cv2.cvtColor(img,colorspaces[index])
    cv2.imshow("color",cv_img)
    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

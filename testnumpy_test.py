import numpy as np
import cv2

cv2.namedWindow("test",cv2.WINDOW_NORMAL)

img = np.zeros((480,640,3),dtype=np.uint8)

# 从矩阵中访问某元素的值
count = 0
while count < 200:
    # BGR
    # img[count,100,1] = 255
    # img[count,100] = [0,0,255] #红色
    img[count,100] = [255,255,255] #白色
    count += 1

cv2.imshow("test",img)

key = cv2.waitKey(0)

if key & 0xFF == ord('q'):   
    cv2.destroyAllWindows()
    

 
#基本功能:
# 可以通过鼠标进行基本图形的绘制
# 1. 可以画线: 当用户按下L键,即选择了画线. 此时, 滑动鼠标即可画线.
# 2. 可以画矩形: 当用户按下R键,即选择了画矩形. 此时, 滑动鼠标即可画矩形.
# 3. 可以画圆: 当用户按下C键,即选择了画圆. 此时, 滑动鼠标即可画圆.
# ....

# curshape: 0-drawline, 1-drawrectangle, 2-drawvcircle


import cv2
import numpy as np

curshape = 0
startpos = (0, 0)

#创建鼠标回调函数
def mouse_Callback(event, x, y, flags, useedata):
    global curshape, startpos

    if(event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x, y)
    elif(event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if curshape == 0: # drawline
            cv2.line(img, startpos, (x, y), (0, 0, 255))
        elif curshape == 1: # drawrectangle
            cv2.rectangle(img, startpos, (x, y), (0, 0, 255))
        elif curshape == 2: # drawcircle
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2 + b**2)**0.5)
            cv2.circle(img, startpos, r, (0, 0, 255))
        else:
            print('error: no shape')
 



#创建窗口
cv2.namedWindow('drawshape', cv2.WINDOW_NORMAL)

#设置鼠标回调
cv2.setMouseCallback('drawshape',mouse_Callback)

#显示窗口和背景
img = np.zeros((480, 640, 3), np.uint8)

while True:
    cv2.imshow('drawshape', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('Q'):
        break
    elif key == ord('L'): # line
        curshape = 0
    elif key == ord('R'): # rectangle
        curshape = 1
    elif key == ord('C'): # circle
        curshape = 2
 
cv2.destroyAllWindows()

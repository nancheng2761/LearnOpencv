import cv2
import numpy as np

img = cv2.imread('./image/kodim20.png')

# Canny(img, minVal, maxVal)
# 使用5 X 5 高斯滤波消除噪声
# 计算图像梯度的方向 (0 / 45 / 90 /135)
# 取局部极大值
dst = cv2.Canny(img, 150, 220)


cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
import cv2
import numpy as np

black = cv2.imread('./image/kodim20.png')
smallcat = cv2.imread('./image/kodim21.png')

# 只有两张图的属性是一样的才可以进行溶合
print(black.shape)
print(black.shape)

# 图像的溶合
# A  A的权重  B  B的权重  静态权重
result = cv2.addWeighted(smallcat, 0.3, black, 0.7, 0)
cv2.imshow('add2', result)
cv2.waitKey(0)
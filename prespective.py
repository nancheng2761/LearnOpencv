import cv2
import numpy as np


# 透视变换
# warpPerspective(img, M, dsize)
img = cv2.imread('./image/kodim21.png')

# getPerspectiveTransform(src, dst)
# 四个点 (图形的四个角)
src = np.float32([[30, 60], [510, 50], [40, 750], [470, 750]]) # 截取
dst = np.float32([[0, 0], [500, 0], [0, 700], [500, 700]]) # 目标尺寸

print(img.shape)

M = cv2.getPerspectiveTransform(src, dst)

new =  cv2.warpPerspective(img, M, (700, 500))

cv2.imshow('kodim', img)
cv2.imshow('new', new)
cv2.waitKey(0)



import cv2
from cycler import V
from matplotlib.ft2font import KERNING
import numpy as np

img = cv2.imread('./image/chess.webp')

# 图像灰度化处理
img1  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 获取卷积核
# getStructuringElement(type, size)  
# size   (3, 3)   (5, 5)
# kernel = np.ones((3, 3), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)) # 全为1的卷积核类型
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))  # 椭圆部分为1的卷积核类型
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 7))  # 十字架部分为1的卷积核类型
print(kernel)

# 腐蚀
# erode(img, kernel, iterations = 1)
# kernel 卷积核   iteration 腐蚀次数
dst = cv2.erode(img1, kernel, iterations = 1)

# 膨胀
# dilate(img, kernelm, iterations = 1)
dst2 =  cv2.dilate(img1, kernel, iterations = 1) 

# 开运算 = 先腐蚀 + 再膨胀  (去除大图形外的小图形)
# morphologyEx(img, cv2.MORPH_OPEN, kernel)
dst3 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)

# 闭运算 = 先膨胀 + 再腐蚀 (去除大图形内的小图形)
# morphologyEx(img, cv2.MORPH_OPEN, kernel)
dst4 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)

# 形态学梯度 (可求图像边缘)
# 梯度 = 原图 - 腐蚀
# morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
dst5 = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)

# 顶帽运算 (用来提取小的区块，得到大图形外的小图形)
# 顶帽 = 原图 - 开运算
# cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
dst6 = cv2.morphologyEx(img1, cv2.MORPH_TOPHAT, kernel)

# 黑帽运算   (用来提取噪点，得到大图形内的小图形)
# 黑帽 = 原图 - 闭运算
# morphologyEx(img1, cv2.MORPH_BLACKHAT, kernel)
dst7 = cv2.morphologyEx(img1, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('img', img)
cv2.imshow('gary', img1) # 图像灰度化处理
# cv2.imshow('dst', dst) # 腐蚀
# cv2.imshow('dst2', dst2) # 膨胀
# cv2.imshow('dst3', dst3) # 开运算
# cv2.imshow('dst4', dst4) # 闭运算
# cv2.imshow('dst5', dst5) # 形态学梯度
# cv2.imshow('dst6', dst6) # 顶帽运算
cv2.imshow('dst7', dst7) # 黑帽运算
cv2.waitKey(0)


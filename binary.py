import cv2
import numpy as np

img = cv2.imread('./image/dog.webp')

# 图像灰度化处理
img1  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 图像全局二值化
# img 最好是灰度图
# thresh 阈值     ret 这个返回值是执行的状态
# 超过阈值，替换成maxVal
ret, dst = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY)
ret, dst2 = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY_INV)

# 自适应二值化
# adaptiveThreshold(img, maxVal, adaptiveMethod, thresholdType, blockSize, C)
# adaptiveMethod 计算阈值的方法
# 有 ADAPTIVE_THRESH_MEAN_C(计算临近区域的平均值) 
# 和 ADAPTIVE_THRESH_GAUSSIAN_C(高斯窗口加权平均值) 两种
# blockSize 邻近区域的大小
# C 常量，应从计算出的平均值或加权平均值中减去 一般为0
# Type  THRESH_BINARY  THRESH_BINARY_INV
dst3 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 0)

cv2.imshow('img', img)
cv2.imshow('gary', img1) # 图像灰度化处理
cv2.imshow('dst', dst) # 图像全局二值化
cv2.imshow('dst2', dst2) # 图像全局二值化-翻转
cv2.imshow('dst23', dst3) # 自适应二值化
cv2.waitKey(0)


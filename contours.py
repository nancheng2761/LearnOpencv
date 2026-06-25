import cv2
from matplotlib.pyplot import gray
import numpy as np

img = cv2.imread('./image/kodim20.png')
print(img.sharp)

# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 轮廓查找
# findContours(img, mode, ApproximationMode)
# 两个返回值， contours (查找到的所有轮廓的列表) 和 hierarchy(层级)
# mode    
#         RETR_EXTERNAL = 0 表示只检测外轮廓
#         RETR_LIST = 1  检测的轮廓不建立等级关系 从里到外，从右到左
#         RETR_CCOMP = 2 每层最多两级  从里到外，从右到左
#         RETR_TREE = 3  按树形存储轮廓 从大到小，从右到左
# ApproximationMode
#         CHAIN_APPROX_NONE    保存所有轮廓上的点
#         CHAIN_APPROX_SIMPLE  只保存角点
# cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.imshow('img', img)
cv2.waitKey(0)
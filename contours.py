import cv2
import numpy as np


img = cv2.imread('./image/mmc.jpg')
img1 = cv2.imread('./image/mmc.jpg')
img2 = cv2.imread('./image/hello.jpg')

# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 图像二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
ret2, binary2 = cv2.threshold(gray2, 150, 255, cv2.THRESH_BINARY_INV)

# 绘制方法
def drawShape(src, points):
    i = 0
    while i < len(points):
        if(i == len(points) - 1):
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        else: 
            x, y = points[i][0]
            x1, y1 = points[i+1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        i = i + 1

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
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv2.findContours(binary2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# 轮廓绘制
# drawContours(img, contours, contourIdx, color, thickness)
# contours 轮廓坐标点
# contourIdx 轮廓顺序选择显示哪个轮廓   -1 表示绘制所有轮廓
# color 颜色(0, 0, 255)
# thickness 线宽 -1 全部填充
# 轮廓绘制
#cv2.drawContours(img, contours, 8, (0, 0, 255), 1)

# 轮廓的面积与周长
# 轮廓面积  contourArea(contour)
# 轮廓周长 arcLength(curve, closed)
#          curve 轮廓     closed  是否是闭合的轮廓
# 计算面积
area = cv2.contourArea(contours[8])
print("area=%d"%(area))
# 计算周长
length = cv2.arcLength(contours[8], True)
print("len=%d"%(length))


# 多边形的逼近与凸包
# 多边形逼近  approxPolyDP(curve, epsilon, closed)
#            curve 轮廓   epsilon  精度   closed 是否是闭合的轮廓
# 凸包 convexHull(points, clockwise)
#      points 轮廓   clockwise 顺时针绘制
# 多边形逼近
e = 20
appeox = cv2.approxPolyDP(contours[8], e, True)
drawShape(img, appeox)
# 凸包
hull = cv2.convexHull(contours[8], True)
drawShape(img1, hull)

# 最小外接矩形
# minAreaRect(points)   points 轮廓    
# 返回值： RotatedRect   (x, y     width, height    angle)
r = cv2.minAreaRect(contours2[0])
box = cv2.boxPoints(r)
box = box.astype(np.int32)
cv2.drawContours(img2, [box], -1, (0, 0, 255), 2)

# 最大外接矩形
# boundingRect(array)   array 轮廓
# 返回值 Rect 
x, y, w, h = cv2.boundingRect(contours2[0])
cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0))


# print(img.shape)
# print(gray.shape)
# print(binary.shape)
# print(contours)
# print(hierarchy)


cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('binary', binary) # 图像二值化
cv2.waitKey(0)

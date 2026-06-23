import cv2
import numpy as np

img = cv2.imread('./image/dog.webp')


# filter(src, ddepth, kernel, anchor, delta, delta, borderType)
# kernel 卷积核
# ddepth 位深 -1 原始位深
# anchor 锚点 默认(-1, -1)
# delta 默认0
# boederType 边界类型 默认
kernel = np.ones((5, 5), np.uint8) / 25

dst = cv2.filter2D(img, -1, kernel)

# 方盒滤波
# normalize = True, a = 1 / W x H  方盒滤波 == 均值滤波
# normalize = False, a = 1  方盒滤波
# boxFilter(src, ddepth, ksize, anchor, normalize, borderType)
# ddepth 输出图像位深     ksize 卷积核大小  anchor  锚点 (核中心点)
dst2 = cv2.boxFilter(img, -1, (5, 5))

# 均值滤波
# cv2.blur(src, ksize, anchor, borderType)
dst3 = cv2.blur(img, (5, 5))

# 高斯滤波
# GaussianBlur(img, kernel, sigmaX, sigmaY)
# kernel 卷积核    sigmaX sigmaY 中型滤波延展宽度
dst4 = cv2.GaussianBlur(img, (5, 5), sigmaX = 1)

# 中值滤波
# 如3 X 3 的卷积核 数组为[1, 2, 2, 4, 6, 8, 9, 10, 12]
# 取其中的中位数作为卷积后的结果值
# medianBlur(img, ksize)  
# ksize 不是“卷积核尺寸元组”，而是核的边长
dst5 = cv2.medianBlur(img, 5)

# 双边滤波 (美颜处理)
# bilateralFilter(img, d, sigmaColor, sigmaSpace)
# d 卷积核大小
dst6 = cv2.bilateralFilter(img, 5, 20, 50)

# 常见的高通滤波
# Sobel (索贝尔) (高斯)  这里如果卷积核的size设为-1,则自动使用Scharr(沙尔)的滤波算法
# Scharr (沙尔) 卷积核固定,3x3的核, 可被Sobel代替
# Sobel 与 Scharr 在计算边缘时只能求一个方向的,要么横轴,要么纵轴   
# 所以Sobel和Scharr在运算完后通常会进行一次加法运算
# Sobel算子
# 先向X方向求导, 然后再向Y方向求导
# 最终结果|G| = |Gx| + |Gy| 

# Laplacian(拉普拉斯) 不用单独求X或Y的边缘, 可以将横轴与纵轴的边缘全部检测出来
# 但是Laplacian(拉普拉斯)对噪音比较敏感, 内部没有降噪的功能
# 在使用Laplacian(拉普拉斯)之前, 我们需要手工进行一次降噪才能更好的发挥效果

cv2.imshow('img', img) 
cv2.imshow('dst', dst) 
cv2.imshow('dst2', dst2) # 方盒滤波
cv2.imshow('dst3', dst3) # 均值滤波
cv2.imshow('dst4', dst4) # 高斯滤波
cv2.imshow('dst5', dst5) # 中值滤波
cv2.imshow('dst6', dst6) # 双边滤波
cv2.waitKey(0) 
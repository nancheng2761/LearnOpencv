import cv2
import numpy as np 

img = cv2.imread('./image/chess.webp')

# 常见的高通滤波
# Sobel (索贝尔) (高斯)  这里如果卷积核的ksize设为-1,则自动使用Scharr(沙尔)的滤波算法
# Scharr (沙尔) 卷积核固定,3x3的核, 可被Sobel代替
# Sobel 与 Scharr 在计算边缘时只能求一个方向的,要么横轴,要么纵轴   
# 所以Sobel和Scharr在运算完后通常会进行一次加法运算

# Laplacian(拉普拉斯) 不用单独求X或Y的边缘, 可以将横轴与纵轴的边缘全部检测出来
# 但是Laplacian(拉普拉斯)对噪音比较敏感, 内部没有降噪的功能
# 在使用Laplacian(拉普拉斯)之前, 我们需要手工进行一次降噪才能更好的发挥效果

# Sobel算子
# 先向X方向求导, 然后再向Y方向求导
# 最终结果|G| = |Gx| + |Gy| 
# Sobel(src, ddepth, dx, dy, ksize = 3, scale = 1, delta = 0, borderType = BORDER_DEFAULT)
# ddepth 输出位深 
# ksize  为 3 5 7 都是可以的, 但为 -1 则自动使用 Scharr (沙尔)的滤波算法
dst = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)  # 索贝尔算子Y方向边缘
dst2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)  # 索贝尔算子X方向边缘
# 进行一次加法运算
# dst3 = dst + dst2
dst3 = cv2.add(dst, dst2) # 最终结果


# Scharr算子
# 与Sobel类似，只是kernel值不同  固定卷积核3x3
# Scharr(src, ddepth, dx, dy, scale = 1, delta = 0)
dst4 = cv2.Scharr(img, cv2.CV_64F, 0, 1, scale = 1, delta = 0) # 沙尔算子Y方向边缘
dst5 = cv2.Scharr(img, cv2.CV_64F, 1, 0, scale = 1, delta = 0) # 沙尔算子Y方向边缘
dst6 = cv2.add(dst4, dst5)

# Laplacian(拉普拉斯)算子
# 可以同时求两个方向的边缘
# 对噪音敏感，一般需要进行去噪再调用拉普拉斯
# Laplacian(img, ddepth, ksize, scale, borderType)
dst7 = cv2.Laplacian(img, cv2.CV_64F, ksize = 5, scale = 1, borderType= cv2.BORDER_DEFAULT)

 
cv2.imshow('img', img)

# cv2.imshow('dst', dst) # 索贝尔算子X方向边缘
# cv2.imshow('dst2', dst2) # 索贝尔算子X方向边缘
# cv2.imshow('dst3', dst3) # 索贝尔最终结果

# cv2.imshow('dst4', dst4) # 沙尔算子Y方向边缘
# cv2.imshow('dst5', dst5) # 沙尔算子Y方向边缘
# cv2.imshow('dst6', dst6) # 沙尔最终结果

cv2.imshow('dst7', dst7) # 拉普拉斯最终结果

cv2.waitKey(0)
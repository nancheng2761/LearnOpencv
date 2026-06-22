import cv2
import numpy as np

dog = cv2.imread('./image/dog.webp')
h, w, ch = dog.shape


# 仿射变换是图像旋转, 平移, 缩放的总称
# warpAffine(src, M, dsize, flags, mode, value)
# M: 变换矩阵    dsize: 输出尺寸大小   flags: 与resize中的插值算法一致
# mode: 边界外推法的标记   value: 填充边界的值 

# 平移矩阵       [[1, 0], [0, 1]]单位矩阵
# 横向移动则改变[1, 0, 100], 竖向移动则改变[0, 1, 200]
M = np.float32([[1, 0, 100], [0, 1, 0]])
new = cv2.warpAffine(dog, M, (w, h))

# 变换矩阵
# getRotationMatrix2D(center,angle,scale)
# center 中心点   angle 角度(逆时针)   scale 缩放比例
# 旋转的角度为逆时针
# M2 = cv2.getRotationMatrix2D((100, 100), 15, 1.0)
# 中心点(X, Y)
M2 = cv2.getRotationMatrix2D((w/2, h/2), 15, 0.5)
new2 = cv2.warpAffine(dog, M2, (w, h))

# 如果想要改变新图像的尺寸,需修改dsize
new3 = cv2.warpAffine(dog, M2, (int(w/2), int(h/2)))

print(new.shape) # 平移矩阵
print(new2.shape) # 变换矩阵
print(new3.shape) # 修改新图像尺寸

# getAffineTransform(src[], dst[])
# 通过三个点可以确定变换的位置
src = np.float32([[40, 30], [80, 30], [40, 100]])
dst = np.float32([[20, 40], [60, 50], [15, 110]])
M3 = cv2.getAffineTransform(src, dst)
new4 = cv2.warpAffine(dog, M3, (w, h))

cv2.imshow('dog', dog) 
cv2.imshow('new', new) # 平移矩阵
cv2.imshow('new2', new2) # 变换矩阵
cv2.imshow('new3', new3) # 修改新图像尺寸
cv2.imshow('new4', new4) # 通过三个点可以确定变换的位置
cv2.waitKey(0)
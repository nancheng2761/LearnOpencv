import cv2
import numpy as np

dog = cv2.imread('./image/dog.webp')

# 图像的放大与缩小
# resize(src, dst, dsize, fx, fy, interpolation)
# dsize 与 fx,fy 输入一个就行
# interpolation 不输入则为默认
# dsize (X, Y)
# new = cv2.resize(dog, (400, 400))
# new = cv2.resize(dog, None, fx = 0.7, fy = 0.7)
new = cv2.resize(dog, None, fx = 1.7, fy = 1.7, interpolation=cv2.INTER_AREA)
print(dog.shape)

cv2.imshow('dog', dog)
cv2.imshow('new', new)
cv2.waitKey(0) 
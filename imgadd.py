import cv2
import numpy as np

dog = cv2.imread('./image/dog.webp')

# 图的加法运算就是矩阵的加法运算
# 因此加法运算的两张图必须是相等的

# 读取图像尺寸数据
#print(dog.shape)

img = np.ones((270, 381, 3), np.uint8) * 50

cv2.imshow('dog', dog)

# 图像加法运算
result = cv2.add(dog, img)
cv2.imshow('result', result)

# 图像减法运算 subtract(A,B) 是A - B
orig_1 = cv2.subtract(dog, img)
cv2.imshow('org_1', orig_1)

# 图像乘法运算 multiply(A, B)
orig_2 = cv2.multiply(dog, img) 
cv2.imshow('org_2', orig_2)

# 图像除法运算 divide(A, B)
orig_3 = cv2.divide(dog, img) * 0.8
cv2.imshow('org_3', orig_3) 

cv2.waitKey(0)
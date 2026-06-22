import cv2
import numpy as np


dog = cv2.imread('./image/dog.webp')

# 图像翻转
# flip(img, fileCode)
# fileCode == 0 上下翻转
# fileCode > 0 左右翻转
# fileCode < 0 上下 + 左右 翻转
new1 = cv2.flip(dog, 0)
new2 = cv2.flip(dog, -1)
new3 = cv2.flip(dog, 1)

cv2.imshow('dog', dog)
cv2.imshow('new1', new1)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)
cv2.waitKey(0)
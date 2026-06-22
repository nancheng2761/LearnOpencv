import cv2
import numpy as np

dog = cv2.imread('./image/dog.webp')

# 图像的旋转
# rotate(img, rotateCode)
new1 = cv2.rotate(dog, cv2.ROTATE_90_CLOCKWISE) #90
new2 = cv2.rotate(dog, cv2.ROTATE_180) # 180
new3 = cv2.rotate(dog, cv2.ROTATE_90_COUNTERCLOCKWISE) # 270

cv2.imshow('dog', dog)
cv2.imshow('new1', new1)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)
cv2.waitKey(0)


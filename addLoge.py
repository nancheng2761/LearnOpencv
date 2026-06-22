# 1. 导入一张图片
# 2. 创建一张Loge
# 3. 计算图片在什么地方添加, 在添加的地方变成黑色
# 4. 利用add, 将Loge 与 图像叠加到一起

import cv2
import numpy as np

# 导入图片
dog = cv2.imread('./image/dog.webp')

# 创建Loge和Mask掩膜
Loge = np.zeros((200, 200, 3), np.uint8)
Mask = np.zeros((200, 200), np.uint8)

# 绘制Loge
Loge[20:120, 20:120] = [0, 0, 255]
Loge[80:180, 80:180] = [0, 255, 0]

Mask[20:120, 20:120] = 255
Mask[80:180, 80:180] = 255

# 对Mask按位求反
m = cv2.bitwise_not(Mask)

# 选择dog添加Loge的位置
roi = dog[0:200, 0:200]

# 与m进行 与操作
tmp = cv2.bitwise_and(roi, roi, mask = m)

dst = cv2.add(tmp, Loge)

dog[0:200, 0:200] = dst

cv2.imshow('dog', dog)
cv2.imshow('dst', dst)
cv2.imshow('tmp', tmp)
cv2.imshow('m', m)
cv2.imshow('Mask', Mask)
cv2.imshow('Loge', Loge)
cv2.waitKey(0)




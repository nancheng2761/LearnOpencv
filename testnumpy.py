import numpy as np

#通过array定义矩阵
a = np.array([1,2,3])
print(a)
b = np.array([[1,2,3],[4,5,6]])
print(b)

#通过zeros定义矩阵
c = np.zeros((8,8,3),np.uint8)
print(c)
#通过ones定义矩阵
d = np.ones((8,8,3),np.uint8)  
print(d)

#通过full定义矩阵
f = np.full((8,8,3), 255, dtype=np.uint8)
print(f)     

#通过identity定义矩阵
g = np.identity(4, dtype=np.uint8)
print(g)

#通过eye定义矩阵
e = np.eye(4,7)
print(e)

h = np.eye(4,7, k=3)
print(h)
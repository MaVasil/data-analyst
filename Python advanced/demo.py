import numpy as np

a=np.array([[1, 2, 3], [4, 5, 6]])
res=a*2
print(res)
b=np.zeros((2, 3))
print(b)
c=np.ones((2, 3))
print(c)
d=np.full((2, 3), 7)
print(d)
e=np.arange(0, 10, 2)
print(e)

print("Shape of a:", a.shape)
print("max of a:", np.max(a))
print("min of a:", np.min(a))
print("mean of a:", np.mean(a))
print("sum of a:", np.sum(a))
import numpy as np
ary = np.random.randint(0, 255, size=(3,4))

print(ary)
print(ary.dtype)
print(ary.ndim)
print(ary.shape)

ary = ary-100
print(ary)
ary = ary + ary
print(ary)

ary1 = np.array([[1,2],[3,4]])
print(ary1+10)

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[100,110]])
print(arr1+arr2)

print(1/ary)
print(ary *5)
print(ary **2)
print(arr1/arr2)
print(arr2/arr1)



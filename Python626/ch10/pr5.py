import numpy as np
ary = np.arange(10)
print(ary)
ary[0]=100
print(ary)

slice1 = ary[2:5]
print(slice1)
print(ary)

value1 = ary[-1]
print(value1)
print(ary)

value2 = ary[-2]
print(value2)
print(ary)

slice2 = ary[:]
print(slice2)
print(ary)

slice1[:] = 77
print(slice1)
print(ary)


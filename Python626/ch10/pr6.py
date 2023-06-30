import numpy as np
# ary = np.arange(10)
# print(ary)
# ary[0]=100

# ary_sub = ary[3:7].copy()
# print(ary_sub)

# ary_sub[:] = 88
# print(ary_sub)

ary1 = np.arange(1,26,1)
ary2 = ary1.reshape(5,5)
print(ary2)
ary3 = ary2.reshape(25)
print(ary3)

ary = np.arange(1,17)
ary = ary.reshape(4,4)
print(ary)

row1=ary[1]
print(row1)

row2=ary[1,0:4]
print(row2)

row3=ary[1,:]
print(row3)
import numpy as np
import random

pList1 = [10, 20, 30, 40]
pList2 = [10, 20, 30, 40.0]

#리스트 -> 넘파이 배열로 변환
numpyAry1 = np.array(pList1)
print(numpyAry1, numpyAry1.dtype)
#리스트 -> 넘파이 배열로 변환
numpyAry1 = np.array(pList2)
print(numpyAry1, numpyAry1.dtype)

numpyAry2 = np.array(pList1, dtype=np.float32)
print(numpyAry2, numpyAry2.dtype)
#5는 인덱스 0,1,2,3,4
numpyAry3 = np.arange(5)
print(numpyAry3, numpyAry3.dtype)

numpyAry4 = np.ones(5)
print(numpyAry4, numpyAry4.dtype)

numpyAry5 = np.ones(5, dtype=np.uint8)
print(numpyAry5, numpyAry5.dtype)

numpyAry6 = numpyAry5.astype(np.float16)
print(numpyAry6, numpyAry6.dtype)
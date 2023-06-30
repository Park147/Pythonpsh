import numpy as np
import random

pythonList = [ np.random.randint(0, 255) for _ in range(5) ]
print('*파이썬 리스트 --> ', pythonList)

numpyAry1 = np.arange(5)
print('*array(pythonList) --> ', numpyAry1)

numpyAry2 = np.arange(3,8)
print('*array(pythonList) --> ', numpyAry2)

numpyAry3 = np.arange(0, 100, 20)
print('array(phthonList) --> ', numpyAry3 )

numpyAry4 = np.ones(5)
print('ones(5) --> \n', numpyAry4 )

numpyAry5 = np.ones((3,4))
print('ones((3,4)) )--> \n', numpyAry5)
#두 함수의 괄호 차이는 함수 호출 시 전달되는 인수의 차이를 나타냅니다. 
# np.ones((3,4))는 (3, 4)라는 튜플을 인수로 받으므로 배열의 크기를 지정하는데 사용됩니다.
#  np.full(5,33)는 두 개의 인수를 받는데, 첫 번째 인수는 배열의 크기 또는 shape이고 두 번째 인수는 배열의 요소로 초기화됩니다. 
# 따라서 괄호 안의 인수의 형식에 따라 함수의 동작이 달라집니다. 
numpyAry8 = np.full(5,33)
print('*full(5,33)-->', numpyAry8)

numpyAry6 = np.zeros(5)
print('*zeors(5)-->', numpyAry6)

numpyAry7 = np.empty(6)
print('*empty(6)-->', numpyAry7)

numpyAry9 = np.identity(5)
print('*identity(5)-->',numpyAry9)


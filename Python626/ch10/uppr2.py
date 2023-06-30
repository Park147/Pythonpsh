import numpy as np

SIZE = 3
numpyAry = np.random.randint(0, 255, size=(SIZE, SIZE))

print(numpyAry)
print()

numpyAry *= 2

print(numpyAry)
print()

sumValue = 0
for i in range(SIZE):
    for k in range(SIZE):
        sumValue += numpyAry[i][k]

print('평균 값 --> %4.2f' % (sumValue / (SIZE*SIZE)))

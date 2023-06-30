import random

SIZE = 5
pythonList = [[random.randint(0, 255) for _ in range(SIZE)] for _ in range(SIZE)]

for i in range(SIZE):
    for k in range(SIZE):
        print("%3d" % pythonList[i][k], end=' ')
    print()
print()

for i in range(SIZE):
    for k in range(SIZE):
        pythonList[i][k] += 100

for i in range(SIZE):
    for k in range(SIZE):
        print("%3d" % pythonList[i][k], end=' ')
    print()
print()

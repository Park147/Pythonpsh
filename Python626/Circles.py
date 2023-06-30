import turtle as t

n = 60  # 원을 60번 그림
t.shape("turtle")
t.speed("fastest")  # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)  # 반지름이 120인 원을 그림
    t.right(360 / n)  # 오른쪽으로 6도 회전

import turtle as t


t.shape("turtle")
t.speed("fastest")  # 거북이 속도를 가장 빠르게 설정
for i in range(300):  # 300번 반복
    t.forward(i)  # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)  # 오른쪽으로 91도 회전

t.done()

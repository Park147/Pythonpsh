import turtle

t = turtle.Pen()
# 도형들
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
for x in range(1, 5):
    t.forward(50)
    t.left(90)

t.reset()
for x in range(1, 9):
    t.forward(100)
    t.left(225)


for x in range(1, 9):
    t.forward(100)
    t.left(225)


t.forward(100)

for x in range(1, 38):
    t.forward(100)
    t.left(175)

t.up()
t.forward(100)
t.down()

for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)

        # 자동차
t.color(1, 0, 0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
t.color(0, 0, 0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)  # -4
t.setheading(0)  # x
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

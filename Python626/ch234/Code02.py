import turtle

# https://docs.python.org/ko/dev/library/turtle.html
import random


# 함수 선언 부분
def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor(r, g, b)
    turtle.pendown()
    rAngle = random.rardrange
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pensize(pSize)
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.right(90)
    turtle.goto(x, y)


def screenRightClick(x, y):
    global r, g, b
    turtle.penup()
    turtle.goto(x, y)
    # penup 마우스 떼는 것


def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pensize(pSize)
    turtle.pencolor((r, g, b))
    turtle


# 변수 선언 부분
pSize = 10
r, g, b = 0.0, 0.0, 0.0

# 메인 코드 부분
screen = turtle.Screen()
image1 = "cat copy.gif"
# screen.addshape(image1)
screen.register_shape("cat copy.gif")
screen.screensize(10, 10)
turtle.title("거북이로 그림 그리기")
turtle.shape(image1)
# turtle.shape("turtle")
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)
# onscreenclick = handleclick listener(kotlin)
turtle.done()

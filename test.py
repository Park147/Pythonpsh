import turtle

# 터틀 창 설정
screen = turtle.Screen()
screen.setup(500, 500)  # 창 크기 설정

# 이미지 로딩
screen.addshape("cat copy.png")  # 이미지 파일 이름을 지정하여 로딩합니다.
turtle.shape("cat copy.png")  # 터틀 모양으로 이미지를 설정합니다.

# 터틀 이동
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.done()  # 터틀 그래픽 창을 유지합니다.

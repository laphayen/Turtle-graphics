#main.py

# import
import turtle
import random


# 마우스 왼쪽 버튼 클릭 시
# x, y 좌표로 r, g, b 색상으로 선을 그린다.
def screenLeftClick(x, y):
	global r, g, b
	turtle.pencolor((r, g, b))
	turtle.pendown()
	turtle.goto(x, y)

# 마우스 오른쪽 버튼 클릭 시
# x, y 좌표로 이동, 선을 그리지 않는다.
def screenRightClick(x, y):
	turtle.penup()
	turtle.goto(x, y)

# 마우스 가운데 버튼 클릭 시
# 거북이의 크기를 랜덤으로 확대/축소한다.
def screenMidClick(x, y):
	global r, g, b
	tSize = random.randrange(1, 10)
	turtle.shapesize(tSize)
	r = random.random()
	g = random.random()
	b = random.random()

# 변수 선언
pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

# 실행부
turtle.title('turtle')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()

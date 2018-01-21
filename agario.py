import turtle
import time
import random
from ball import Ball
turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []
for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	if dx ==0:
		dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	if dy ==0:
		dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
MY_BALL = Ball(x,y,dx,dy,r,(random.random(), random.random(), random.random()))
BALLS.append(MY_BALL)

def move_all_balls():
	for a in BALLS:
		a.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def collide(ball_a, ball_b):
	if (ball_a.shapesize()[0]*10 + ball_b.shapesize()[0]*10) >= (math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+(math.pow(ball_a.ycor()-ball_b.ycor(),2)))):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				r1 = ball_a.r
				r2 = ball_b.r
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			new_dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			while new_dx==0 or new_dy==0:
				new_dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				new_dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			new_r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			Color = (random.random(), random.random(), random.random())
			if (r1<r2):
				ball_a.x = new_x
				ball_a.y = new_y
				ball_a.dx = new_dx
				ball_a.dy = new_dy
				ball_a.r = new_r
				ball_a.color(Color)
				ball_b.r=ball_b.r+1
				ball_b.shapesize(new_r/10)
			if (r2<r1)
				ball_b.x = new_x
				ball_b.y = new_y
				ball_b.dx = new_dx
				ball_b.dy = new_dy
				ball_b.r = new_r
				ball_b.color(Color)
				ball_a.r=ball_a.r+1
				ball_a.shapesize(new_r/10)

def check_myball_collision():
	for a in BALLS:
		if collide(ball_a,MY_BALL)==True:
			r3 = a.r
			r4 = MY_BALL.r
		if (r4<r3):
			MY_BALL.x = new_x
			MY_BALL.y = new_y
			MY_BALL.dx = new_dx
			MY_BALL.dy = new_dy
			MY_BALL.r = new_r
			MY_BALL.color(Color)
			MY_BALL.r=ball_a.r+1
			MY_BALL.shapesize(new_r/10)
			return False
		if (r3<r4):
			a.x = new_x
			a.y = new_y
			a.dx = new_dx
			a.dy = new_dy
			a.r = new_r
			a.color(Color)
			a.r=ball_a.r+1
			a.shapesize(new_r/10)
	return True

def movearound(event):
	MY_BALL.X = event.x - screen’s width
	MY_BALL.y = screen’s height - event.y
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


while RUNNING == True:
	
	if (SCREEN_WIDTH != canvas.width()/2):
		SCREEN_WIDTH = canvas.width()/2
	if (SCREEN_HEIGHT != canvas.height()/2):
		SCREEN_HEIGHT = canvas.height()/2
	move_all_balls()
	check_all_balls_collision()
	MY_BALL.movearound()
	while MY_BALL.check_myball_collision()== False:
		
import turtle
from turtle import Turtle
import time
import random
from ball import Ball
import math

turtle.tracer(0)
turtle.hideturtle()

RUNNING = True
SLEEP = 0.1
#0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width() / 2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height() / 2

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 50
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []

MY_BALL1 = Ball(0, 0, 0, 0, 20, ("blue"))

for i in range(NUMBER_OF_BALLS):
    x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    if dx == 0:
        dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    if dy == 0:
        dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
    #radius = 30+i
    color = (random.random(), random.random(), random.random())
    BALL = Ball(x, y, dx, dy, radius, color)
    BALLS.append(BALL)


def move_all_balls():
    for a in BALLS:
        a.move(SCREEN_WIDTH, SCREEN_HEIGHT)


def collide(ball_a, ball_b):
    if ball_a == ball_b:
        return False
    if ((ball_a.radius + ball_b.radius) >=  math.sqrt( math.pow(ball_a.xcor() - ball_b.xcor(), 2) + math.pow(ball_a.ycor() - ball_b.ycor(), 2) )):
        return True
    else:
        return False


def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a, ball_b) == True:
                r1 = ball_a.radius
                r2 = ball_b.radius
                new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                if new_dx == 0:
                    new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                if new_dy == 0:
                    new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                new_color = (random.random(), random.random(), random.random())
                if (r1 > r2):
                    ball_b.goto(new_x, new_y)
                    ball_b.setdx(new_dx)
                    ball_b.setdy(new_dy)
                    ball_b.setRadius(new_radius)
                    ball_b.setColor(new_color)
                    r1 += 10
                    ball_a.setRadius(r1)
                if (r2 > r1):
                    ball_a.goto(new_x, new_y)
                    ball_a.setdx(new_dx)
                    ball_a.setdy(new_dy)
                    ball_a.setRadius(new_radius)
                    ball_a.setColor(new_color)
                    r2 += 10
                    ball_b.setRadius(r2)

def check_myball_collision():
    for ball_a in BALLS:
        if collide(ball_a, MY_BALL1) == True:
            r3 = ball_a.radius
            r4 = MY_BALL1.radius
            new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
            new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
            new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
            if new_dx == 0:
                new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
            new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
            if new_dy == 0:
                new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
            new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
            new_color = (random.random(), random.random(), random.random())
            if (r3 > r4):
                MY_BALL1.goto(new_x, new_y)
                MY_BALL1.setdx(new_dx)
                MY_BALL1.setdy(new_dy)
                MY_BALL1.setRadius(new_radius)
                MY_BALL1.setColor(new_color)
                r3 += 10
                ball_a.setRadius(r3)
            if (r4 > r3):
                ball_a.goto(new_x, new_y)
                ball_a.setdx(new_dx)
                ball_a.setdy(new_dy)
                ball_a.setRadius(new_radius)
                ball_a.setColor(new_color)
                r4 += 10
                MY_BALL.setRadius(r4)


def movearound(event):
    MY_BALL1.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)


turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING:
#    if SCREEN_HEIGHT != turtle.getcanvas().winfo_height() / 2 or SCREEN_WIDTH != turtle.getcanvas().winfo_width() / 2:
#        SCREEN_HEIGHT = turtle.getcanvas().winfo_height() / 2
#        SCREEN_WIDTH = turtle.getcanvas().winfo_width() / 2

    move_all_balls()
    check_all_balls_collision()
    check_myball_collision()    
    #MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    #turtle.getscreen().update()
    turtle.update()
    time.sleep(SLEEP)
    #turtle.mainloop()
from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)



a = Ball(8,"blue", 1)
b = Ball(10,"green", 1)
a.penup()
b.penup()
a.goto(100,100)
b.goto(-100,-100)
a.goto(-100,-100)
def Check_collision(a,b):
	if (a.shapesize()+b.shapesize())<=(Math.sqrt(Math.pow(a.xcor()-b.xcor(),2)+(Math.pow(a.ycor()-b.ycor(),2)))):
		a.color("green")
		b.color("blue")
		turtle.write("collision!!!!!!!!")
Check_collision(a,b)
mainloop()
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
class Reckt(Turtle):
	def __init__(self, heigth, width, color, speed):
		Turtle.__inist__(self)
		shape = turtle.registershape((0,0), (heigth,0), (heigth,width), (0,width))
		self.shape(shape)
		self.color(color)
		self.speed(speed)
bob = Reckt(10,20,"gray", 20)



a = Ball(10,"blue", 1)
b = Ball(10,"green", 1)
w = Ball(0.01,"green", 1)
w.hideturtle()
a.penup()
b.penup()
a.goto(100,100)
b.goto(100,0)
a.goto(50,0)
def Check_collision(a,b):
	if (a.shapesize()[0]*10+b.shapesize()[0])*10 >= (math.sqrt(math.pow(a.xcor()-b.xcor(),2)+(math.pow(a.ycor()-b.ycor(),2)))):
		a.color("red")
		b.color("black")
		w.write("collision!!!!!!!!",font=("Arial", 20, "normal"))
	else:
		w.write("no collision!!!!!!!!",font=("Arial", 20, "normal"))


Check_collision(a,b)
mainloop()

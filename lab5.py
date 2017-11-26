
from turtle import *
import random
colormode(255)
class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		register_shape("myRectangle", ((0,0), (width,0), (width,height), (0,height)))
		self.shape("myRectangle")
class Square(Rectangle):
	def __init__(self, size):
		Rectangle.__init__(self,width,height)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)	
		b = random.randint(0,255)	
		self.color(r,g,b)
sq1 = Square(50,100,100)
mainloop()

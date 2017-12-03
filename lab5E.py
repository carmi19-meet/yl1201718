from turtle import *
class hex(Turtle):
	def __init__(self, size,lines):
		Turtle.__init__(self)
		self.hideturtle()
		self.speed(100000)
		self.shapesize(size)
		self.begin_poly()
		for i in range(lines):
			self.penup()
			self.fd(size)
			self.left(180-((180*lines-360)/lines))
		self.end_poly()
		p = self.get_poly()
		register_shape("myFavouriteShape", p)
		self.shape("myFavouriteShape")
		self.showturtle()

a = hex(10,8)
#a.goto(-100,100)
mainloop()
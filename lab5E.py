from turtle import *
class hex(Turtle):
	def __init__(self, size,lines):
		Turtle.__init__(self)
		self.hideturtle()
		self.shapesize(size)
		self.begin_poly()
		for i in range(lines):
			self.penup()
			self.fd(size)
			self.left(60)
		self.end_poly()
		p = self.get_poly()
		register_shape("myFavouriteShape", p)
		self.shape("myFavouriteShape")
		self.showturtle()

a = hex(9,6)
a.goto(-100,100)
mainloop()
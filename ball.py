from turtle import *

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)

	def move(self,screen_width,screen_height):
		current_x = xcor()
		current_y = ycor()
		new_x = current_x + self.dx
		new_y = current_y +self.dy

		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_x + self.r
		
		

		if (left_side_ball<=-(screen_width/2)):
			new_x = current_x
		else:
			new_x = current_x +self.dx
		
		if (right_side_ball>=(screen_width/2)):
			new_x = current_x
		else:	
			new_x = current_x -self.dx
		if (top_side_ball>=(screen_height/2)):
			new_y = current_y
		else:
			new_y = current_y - self.dy
		if (bottom_side_ball<=-(screen_height/2)):
			new_y = current_y
		else:
			new_y = current_y + self.dy
		self.goto(new_x,new_y)
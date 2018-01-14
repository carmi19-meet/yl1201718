from turtle import *

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.___init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color = color
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)

def move(self,screen_width,screen_height):
		current_x = x_cor()
		current_y = y_cor()
		new_x = current_x +dx
		new_x = current_x +dx

		right_side_ball = new_x + r
		left_side_ball = new_x - r
		top_side_ball = new_y + r
		bottom_side_ball = new_x + r
		self.goto(new_x,new_y)
		

		if (left_side_ball<=-(screen_width/2)):
			new_x = current_x
		else:
				new_x = current_x +dx
		if (right_side_ball>=(screen_width/2)):
			new_x = current_x
		else:
			new_y = current_y + dy
		if (top_side_ball>=(screen_height/2)):
			new_y = current_y
		else:
			new_y = current_y + dx
		if (bottom_side_ball<=-(screen_height/2)):
			new_y = current_y
		else:
			new_y = current_y + dx
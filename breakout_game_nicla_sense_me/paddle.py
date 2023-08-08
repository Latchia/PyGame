from turtle import Turtle

MOVE_DIST = 100


class Paddle(Turtle):
	def __init__(self,screen_width):
		super().__init__()
		self.color('dark goldenrod')
		self.shape('square')
		self.penup()
		self.shapesize(stretch_wid=1, stretch_len=10)
		self.goto(x=0, y=-280)
		self.screen_width = screen_width

	def move_left(self):
		new_x = self.xcor() - MOVE_DIST
		if new_x > - self.screen_width / 2 +50 :
			self.goto(new_x,self.ycor())

	def move_right(self):
		new_x = self.xcor() + MOVE_DIST
		if new_x < self.screen_width / 2 - 50 :
			self.goto(new_x,self.ycor())


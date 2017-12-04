from turtle import *
import random
class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1=ball(10,"green",5)
ball2=ball(8,"pink",5)

def ckeck_collision(ball1, ball2):
	d=math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2))+math.pow((ball1.ycor()-ball2.ycor(),2))
	if d<=ball1.shapesize()[0]+ball2.shapesize()[0]:
	ball1.color= blue




from turtle import *
import random
import math
class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1=Ball(10,"green",5)
ball2=Ball(8,"pink",5)
ball3=Ball(4,"red",5)

def ckeck_collision(ball1, ball2):
	d=math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow((ball1.ycor()-ball2.ycor()),2))
	if d<=ball1.radius+ball2.radius:
		ball1.color("blue")

#ball2.goto(7,8)
#ckeck_collision(ball1, ball2)
list1 = [ball1,ball2,ball3]

def check_collision2(list1):
	for i in range(len(list1)):
		for j in range(i+1, len(list1)):
			if ckeck_collision( list1[i], list1[j]):
				if list1[i].radius<list1[j].radius:
					#print("the ball number:"+str(i)+"is smaller than the ball number:"+str(j))
					list1[i].goto(random.
				else
			 		#list1[j].radius<list1[i].radius:
					#print("the ball number:"+str(j)+"is smaller than the ball number:"+str(i))
					list1[j].goto(random.randint(20, 201), random.randint(30, 201))			

mainloop()



 

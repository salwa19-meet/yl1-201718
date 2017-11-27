from turtle import *
import random 
colormode(255)

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)

	def random_color(self):
		r = random.randint(0, 256)
		g = random.randint(0, 256)
		b = random.randint(0, 256)
		self.color(r, g, b)
	
square1 = Square(30)
square1.random_color()
#########################



class Hexagon(Turtle):
	def __init__(self,size,color):
		Turtle.__init__(self)
		self.begin_poly()
		self.color(color)
		self.speed('slow')ee
		self.begin_fill()
		for i in range(6):

			self.forward(size)				
			self.right(360/6)
		self.end_fill()
		self.end_poly()
	 	register_shape("Hex", self.get_poly())
	 	

hexagon = Hexagon(50,"red")

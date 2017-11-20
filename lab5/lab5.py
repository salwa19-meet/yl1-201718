from turtle import Turtle, colormode

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
square1.random_color(r,g,b)



		
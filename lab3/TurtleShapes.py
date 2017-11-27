from turtle import *
import turtle
import random 
colormode(255)
'''
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.goto(100,50)
turtle.goto(150,25)
turtle.penup()
turtle.mainloop()'''



turtle.pendown()
turtle.forward(100)
turtle.right(45)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)

turtle.speed(0)
for i in range(360):
	turtle.right(i)
	turtle.pendown()
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	turtle.color(r,g,b)
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(25)
	turtle.home()
	


	turtle.right(1)



turtle.mainloop()
from turtle import*
import random

shape("turtle")
speed(10)
pensize(2)

Screen().bgcolor("white")
colours = ["fuchsia", "yellow", "lime", "pink", "orange", "red", "blue", "darkorchid", "brown", "turquoise", "lightsalmon", "silver"]

def vshape(size):
	right(25)
	forward(size)
	backward(size)
	left(50)
	forward(size)
	backward(size)
	right(25)

def snowflakeArm(size):
	for x in range(0,4):
		forward(size)
		vshape(size)
	backward(size*4)

def snowflake(size):
	for x in range(0,6):
		snowflakeArm(size)
		right(60)
		

for i in range(0,30):
	color(random.choice(colours))
	size = random.randint(5,30)
	x = random.randint(-400,400)
	y = random.randint(-400,400)
	penup()
	goto(x,y)
	pendown()
	snowflake(size)
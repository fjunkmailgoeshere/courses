#!/usr/bin/python

import turtle



def draw_flower(theturtle):

	for i in range(1,37):
		theturtle.left(35)
		theturtle.forward(50)
		theturtle.right(35)
		theturtle.forward(50)
		theturtle.right(145)
		theturtle.forward(50)
		theturtle.right(35)
		theturtle.forward(50)
		theturtle.right(10)

	#draw stem
	theturtle.right(90)
	theturtle.forward(200)


	#brad.left(90)
	#brad.forward(100)
	#brad.left(90)
	#brad.forward(50)
	#brad.right(90)

	#loopcount = 72
	#for i in range(0,loopcount):
	#	brad.right(360.0/loopcount)
	#	brad.forward(100)
	#	brad.right(90)

	#brad.right(45)
	#brad.forward(70)

	#loopcount = 72
	#for i in range(0, loopcount):
	#	brad.right(


def draw_triangle(theturtle, length, ori, recursion):
	recursion = recursion + 1
	
	for i in range(0,3):
		if(recursion<4):
			#if (0):
			theturtle.forward(length/2)
			theturtle.left(120)
			draw_triangle(theturtle,length/2,0,recursion)
			theturtle.right(120)
			theturtle.forward(length/2)
		else:
			theturtle.forward(length)
		if (ori==1):
			theturtle.left(120)
		else:
			theturtle.right(120)


window = turtle.Screen()
window.bgcolor("red")

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow","pink")
brad.speed(10)
startx = brad.xcor()
starty = brad.ycor()

draw_flower(brad)

#brad.setpos(brad.xcor()+300, brad.ycor())
brad.penup()
brad.setpos(startx+250,starty+25)
brad.pendown()

brad.right(30)
draw_triangle(brad,200,1,0)

window.exitonclick()


draw_turtles(brad)

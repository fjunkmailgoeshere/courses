#!/usr/bin/python

import turtle



def draw_turtles():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow","pink")
	brad.speed(2)

	for i in xrange(0,4):
		brad.forward(100)
		brad.right(90)


	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

	ralph = turtle.Turtle()
	ralph.shape("classic")
	ralph.color("white")
	ralph.speed(9)


	i = 0
	while i < 3:
		print i
		ralph.forward(100)
		ralph.right(120)
		i += 1

	window.exitonclick()


draw_turtles()

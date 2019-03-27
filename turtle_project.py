
import turtle

def draw_square(square):
	for x in range(4):
		square.forward(150)
		square.right(90)

def square_circle(square):
	n = 0
	while n < 80:
		square.circle(100)
		square.right(5)
		n += 1

def move_square():
	window = turtle.Screen()
	window.bgcolor("yellow")

	creature = turtle.Turtle()
	creature.shape("arrow")
	creature.speed(20)
	creature.pensize(2)
	creature.shapesize(2)
	creature.color("red")

	for i in range(75):
		draw_square(creature)
		creature.right(5)


	angel = turtle.Turtle()
	angel.color("green")
	angel.pensize(2)
	angel.speed(25)
	angel.shape("turtle")
	square_circle(angel)


	window.exitonclick()

move_square()
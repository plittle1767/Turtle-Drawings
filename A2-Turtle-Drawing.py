from turtle import *

window = Screen()
turtle = Turtle()
turtle.speed(0)

#
# CS 1400 Assignment 2. Written by David Johnson and Preston Little
# This code, as it is now or after modification, may not be shared or uploaded to any public site.
# It may be uploaded to the course approved assignment submission system.

# Draw a square with a Python turtle.
# Do not modify this.
def draw_square():
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

# Draw a wall of ten blocks with a little space between each one.
def draw_wall():
    turtle.penup()
    turtle.goto(-150, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(-120, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(-90, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(-60, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(-30, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(0, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(30, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(60, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(90, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

    turtle.penup()
    turtle.setposition(120, 250)
    turtle.pendown()
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)

# Draw a simple face with a head and two eyes.
def draw_face():
# this will be the face
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.circle(50)

# this will be the eyes
    turtle.penup()
    turtle.goto(-20, 160)
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(20, 160)
    turtle.pendown()
    turtle.dot(10)

# this will be the mouth
    turtle.penup()
    turtle.goto(-15, 130)
    turtle.pendown()
    turtle.forward(30)

# the repeating shape will be rectangles
def scene_shape():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("red")
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(125)

# second rectangle
    turtle.penup()
    turtle.goto(-10, -100)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("red")
    for side in range(2):
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(125)

# the shapes defined her are triangles for the roof of the houses
def scene_roof():
    turtle.penup()
    turtle.goto(-110, 25)
    turtle.pendown()
    turtle.pensize(7)
    turtle.color("brown")
    turtle.right(240)
    turtle.forward(58)
    turtle.left(300)
    turtle.forward(58)

    turtle.penup()
    turtle.goto(0, 25)
    turtle.pendown()
    turtle.pensize(7)
    turtle.right(300)
    turtle.forward(58)
    turtle.left(300)
    turtle.forward(58)

# the scene I drew was of two tall houses with a sun in the background
def draw_scene():
    turtle.penup()
    turtle.goto(-500, -100)
    turtle.pendown()
    turtle.forward(1000)

    turtle.penup()
    turtle.goto(-300, 25)
    turtle.pendown()
    turtle.circle(75)


draw_wall()

draw_face()

draw_scene()

scene_shape()

scene_roof()

turtle.hideturtle()  # Get rid of the arrow showing the turtle location.

window.exitonclick()
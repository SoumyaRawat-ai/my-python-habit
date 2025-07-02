import random
import turtle
from turtle import Turtle, Screen, colormode
import colorgram

turtle.colormode(255)
colors = colorgram.extract('download (1).jpeg', 20)
rgb_color = [
    (247, 236, 37),
    (239, 39, 152),
    (36, 216, 77),
    (39, 79, 185),
    (28, 39, 159),
    (210, 73, 16),
    (218, 140, 198),
    (223, 159, 61),
    (17, 151, 18),
    (239, 231, 3)
]

chose_color = random.choice(rgb_color)


timmy = Turtle()
timmy.hideturtle()
timmy.penup()
y = -200
for i in range(10):
    y += 50
    timmy.setpos(-200,y)
    for n in range(10):
        timmy.dot(20, random.choice(rgb_color))
        timmy.forward(50)






















Screen = Screen()
Screen.exitonclick()
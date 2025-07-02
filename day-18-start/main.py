# import random
# import turtle
# from turtle import Turtle, Screen, speed
#
# timmy = Turtle()
# timmy.speed("fastest")
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     random_color1 = (r, g, b)
#     return random_color1
#
#
# def draw_spirograph(size_of_gap):
#     for i in range(int(360/ size_of_gap)):
#         timmy.circle(100)
#         timmy.color(random_color())
#         timmy.setheading(timmy.heading() + size_of_gap)
#
# draw_spirograph(5)
#
#
# screen = Screen()
# screen.exitonclick()

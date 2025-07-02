import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")

timmy.color("red")  # Change the turtle color here
# timmy.position()
timmy.forward(100)
my_screen = turtle.Screen()
# my_screen.canvheight = 900
print(my_screen.canvheight)
my_screen.exitonclick()

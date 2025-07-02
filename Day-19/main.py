from turtle import Turtle, Screen

Timmy = Turtle()
screen = Screen()


def move_forward():
    Timmy.forward(10)
def move_backwards():
    Timmy.backward(10)
def counter_clock():
    new_heading =Timmy.heading() + 10
    Timmy.setheading(new_heading)
def clockwise():
    new_heading = Timmy.heading() - 10
    Timmy.setheading(new_heading)
def clear_screen():
    Timmy.home()
    Timmy.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

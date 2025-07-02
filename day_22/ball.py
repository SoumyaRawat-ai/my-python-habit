from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.color('blue')
        self.penup()
        self.shape('circle')
        self.goto(0,0)

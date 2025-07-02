from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def move_upward(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_downward(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
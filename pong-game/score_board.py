from turtle import Turtle


class Score_board(Turtle):
    def __init__(self, score1, score2):
        super().__init__()
        self.score1 = score1
        self.score2 = score2
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        while self.ycor() < 260:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.create_board()
    def create_board(self):
        self.write(f"{self.score1} : {self.score2}", align="center", font=("Courier", 25, "bold"))

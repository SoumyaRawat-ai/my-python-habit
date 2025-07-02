from turtle import Screen, Turtle

screen = Screen()

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0

    def score_board(self):
        self.goto(0, -280)
        self.setheading(90)
        self.hideturtle()
        for i in range(27):
            self.forward(10)
            self.color("white")
            self.forward(10)
            self.color("black")
        self.color('white')
        self.penup()


    def write_score(self):
        self.write(f'Score {self.score1} : {self.score2}', font = ("Arial", 16, "bold"), align='center' )
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.high_score = 0
    def score(self):
        self.goto(0, 265)
        self.pendown()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_score()

    def reset(self):
        if self.Score > self.high_score:
            self.high_score = self.Score
            with open('example.txt', 'w') as file:
                file.write(f'{self.high_score}')
        self.Score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        with open('example.txt', 'r') as file:
            a = file.read()
        self.write(f"Score : {self.Score} High Score : {a}", align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.Score += 1
        self.clear()
        self.update_score()

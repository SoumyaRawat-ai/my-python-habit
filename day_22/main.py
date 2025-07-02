from turtle import Turtle, Screen
from pandel import Pandel
from score_board import Score_board
from ball import Ball
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()
padel = Pandel()
padel.speed('fastest')
screen.onkey(padel.move, 'Up')
screen.onkey(padel.move_backward, 'Down')

ball = Ball()

score = Score_board()
score.speed('fastest')
score.score_board()
score.write_score()

screen.exitonclick()
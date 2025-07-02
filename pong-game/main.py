from turtle import  Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Score_board

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title("Pong")

screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))

ball = Ball()
screen.listen()
screen.onkeypress(r_paddle.move_upward, 'Up')
screen.onkeypress(r_paddle.move_downward, 'Down')

screen.onkeypress(l_paddle.move_upward, 'w')
screen.onkeypress(l_paddle.move_downward, 's')

score1 = 0
score2 = 0

score = Score_board(score1, score2)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    screen.update()
    if ball.ycor() >285 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) <50 and ball.xcor() >350 or ball.distance(l_paddle) < 50 and ball.xcor() < - 350:
        ball.bounce_x()
        ball.speed(10)

    if ball.xcor() > 400:
        ball.ball_reset()
        score1 += 1
        score.clear()
        score = Score_board(score1, score2)

    if ball.xcor() < -400:
        ball.ball_reset()
        score2 += 1
        score.clear()
        score = Score_board(score1, score2)


screen.exitonclick()
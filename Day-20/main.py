import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
Score_Board = ScoreBoard()
Score_Board.score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        Score_Board.increase_score()


    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()> 290 or snake.head.ycor() < -290 :
        Score_Board.reset()
        snake.reset()


    #Detect collides with tail
    for segment in snake.new_turtle[1:]:
        if snake.head.distance(segment) <10:
            Score_Board.reset()
            snake.reset()
    # if head collides with any segment in tail:
     # trigger game_over





screen.exitonclick()
from turtle import Turtle
dis = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE =20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.new_turtle = []
        self.create_snake()
        self.head = self.new_turtle[0]

    def create_snake(self):
        for position in dis:
            self.add_segment(position)

    def move(self):
        for i in range(len(self.new_turtle) - 1, 0, -1):
            new_x = self.new_turtle[i - 1].xcor()
            new_y = self.new_turtle[i - 1].ycor()
            self.new_turtle[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
            timmy = Turtle("square")
            timmy.color('white')
            timmy.penup()
            timmy.goto(position)
            self.new_turtle.append(timmy)
    def reset(self):
        for seg in self.new_turtle:
            seg.goto(1000, 1000)
        self.new_turtle.clear()
        self.create_snake()
        self.head = self.new_turtle[0]

    def extend(self):
        self.add_segment(self.new_turtle[-1].position())
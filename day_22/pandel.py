from turtle import Turtle
class Pandel(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        self.position = [(-290, 0), (-290, -20), (-290, 20), (-290, 40)]
        self.position_two = [(285, 0), (285, -20), (285, 20), (285, 40)]
        self.create_padel()
        self.create_pandel2()

    def create_padel(self):
        for i in self.position:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(i)
            self.segment.append(segment)

    def create_pandel2(self):
        for i in self.position_two:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(i)

    def move(self):
        b = True
        while b:
            for i in self.segment:
                i.setheading(90)
                i.forward(10)
                a = False

    def move_backward(self):
        a = True
        while a:
            for i in self.segment:
                i.setheading(270)
                i.forward(10)
                b = False
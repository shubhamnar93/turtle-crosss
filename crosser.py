from turtle import Turtle, Screen


class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-220)
        self.setheading(90)
    def move(self):
        self.fd(30)
        # Screen().update()
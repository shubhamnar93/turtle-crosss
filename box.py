import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
class Box(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.sety(random.randint(-200,200))
        self.setx(280)



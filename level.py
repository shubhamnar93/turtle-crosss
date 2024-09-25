from turtle import Turtle, Screen


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_number=0
        self.goto(x= -270, y= 220)

    def level_up(self):
        self.level_number+=1
        self.clear()
        self.write(f"level: {self.level_number}", align="center", font=('Arial', 10, 'bold'))

    def game_over(self):
        self.home()
        self.write(f"Game over", align="center", font=('Arial', 24, 'bold'))


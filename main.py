import time
from time import sleep

from level import Level
from turtle import Turtle,Screen
from box import Box
from crosser import Crosser

screen = Screen()
turtle = Crosser()
screen.setup(width=600, height=500)
screen.tracer(0)
game = True
box=[]
m=0
screen.listen()
screen.onkey(turtle.move, "w")

level = Level()
level.level_up()
sleep_time=0.03

while game:

    box.append(Box())
    time.sleep(0.1)
    for i in box[m:]:

        if i.xcor()>-300:
            i.setx(i.xcor()-20)
        else:
            m+=1

        if turtle.distance(i)<30:
            level.game_over()
            game=False

        screen.update()
        time.sleep(sleep_time)

    if turtle.ycor()>220:
        level.level_up()
        turtle.sety(-220)
        sleep_time*=0.9


screen.exitonclick()


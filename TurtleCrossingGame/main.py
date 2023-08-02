

from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
screen =  Screen()
screen.bgcolor("white")
screen.setup(600,600)
screen.title("TurtleCrossingGame")

screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = ScoreBoard()
# turt = Turtle("turtle")
# turt.color("Blue")
# turt.penup()
# turt.goto(0,-280)
# turt.setheading(90)
screen.listen()
screen.onkey(player.move, "Up")
#turt.forward(10)

gam_on = True
while gam_on:
    time.sleep(player.sp)
    screen.update()
    car.make_cars()
    car.gotoo()
    for c in car.all_turt:
        if c.distance(player)<20:
            gam_on = False
            scoreboard.gameover()
    if player.ycor() > 280:
        player.reset()
        scoreboard.point()
        car.levelup()
screen.exitonclick()


from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)
screen.listen()
timmy = Turtle()
timmy.color("White")
timmy.speed(0)
timmy.penup()
timmy.goto(0,300)
timmy.pensize(3)
timmy.setheading(270)


for _ in range(25):
    timmy.pendown()
    timmy.forward(12)
    timmy.penup()
    timmy.forward(12)

rpaddle = Paddle((350,0))
lpaddle = Paddle((-350,0))
ball = Ball()
scoreboard  = Scoreboard()
# def go_u():
#     new_y = zimmy.ycor() + 20
#     zimmy.goto(zimmy.xcor(),new_y)
#
# def go_d():
#     new_y = zimmy.ycor() - 20
#     zimmy.goto(zimmy.xcor(), new_y)

screen.onkey(rpaddle.go_up,"Up")
screen.onkey(rpaddle.go_down,"Down")

screen.onkey(lpaddle.go_up,"W")
screen.onkey(lpaddle.go_down,"A")

game_is_on = True
while game_is_on:
    time.sleep(ball.sp)
    screen.update()
    ball.move()
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.ybounce()

    if ball.distance(rpaddle)<50 and ball.xcor()>320 or ball.distance(lpaddle)<50 and ball.xcor()<-320 :
        ball.xbounce()


    if ball.xcor()>370 :
        ball.reset()
        scoreboard.lpoint()

    if ball.xcor()<-370:
        ball.reset()
        scoreboard.rpoint()


screen.exitonclick()

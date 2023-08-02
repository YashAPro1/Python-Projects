from turtle import  Turtle,Screen
import random
from food import Food
import time
from snake import Snake
from score import Scoreboard


screen = Screen()
food = Food()
score=Scoreboard()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or \
            snake.segments[0].ycor()<-290:
        is_game_on=False
        score.game_over()
    for turtle in snake.segments:
        if turtle== snake.head:
            pass
        elif snake.head.distance(turtle)<10:
            is_game_on=False
            score.game_over()


screen.exitonclick()
STARTING_POSITION = (0,-280)
MOVE_DIST = 10
FINISHLINE = 280
from turtle import Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.sp = 0.1

    def move(self):
        self.forward(MOVE_DIST)

    def reset(self):
        self.goto(STARTING_POSITION)
        self.sp *= 0.9


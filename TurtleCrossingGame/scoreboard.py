FONT = ("Courier",24,"normal")
from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("brown")
        self.hideturtle()
        self.w = "Game over!"
        self.score = 0

    def gameover(self):
        self.goto(0,0)
        self.write(self.w,align="center",font=FONT)

    def point(self):
        self.clear()
        self.level += 1
        self.score += 1
        self.goto(0,260)
        self.write(f"Score: {self.score}, Level = {self.level}", align="center", font=FONT)

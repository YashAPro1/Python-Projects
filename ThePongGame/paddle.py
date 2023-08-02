from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.position=position
        self.shape("square")
        self.color("White")
        self.speed(0)
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(self.position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
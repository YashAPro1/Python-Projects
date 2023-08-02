import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.x=0
        self.y = 0
        self.x_move = 10
        self.ymove = 10
        self.sp = 0.1
        

    def move(self):
        new_x = self.xcor() +self.x_move
        new_y = self.ycor() +self.ymove
        self.goto(new_x,new_y)




    def ybounce(self):
        self.ymove *= -1

    def xbounce(self):
        self.x_move *= -1
        self.sp *= 0.9

    def reset(self):
        self.goto(self.x,self.y)
        self.sp = 0.1
        self.xbounce()



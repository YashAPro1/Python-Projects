COLORS = ["red","orange","yellow","green","blue","purple"]
STRT_MOV = 5
MOV_INCREMET = 10
from turtle import Turtle
import random
class CarManager():

    def __init__(self):
        super().__init__()
        self.all_turt = []
        self.sp = 0.1
        self.speed = STRT_MOV



    def make_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            turt = Turtle()
            turt.penup()
            turt.color(COLORS[random.randint(0,5)])
            turt.setheading(180)
            turt.shape("square")
            turt.shapesize(stretch_wid=1, stretch_len=2)
            newy = random.randint(-240,240)
            turt.goto(260, newy)
            self.all_turt.append(turt)


    def gotoo(self):
        for turt in self.all_turt:
            turt.forward(self.speed)

    def levelup(self):
        self.speed += MOV_INCREMET



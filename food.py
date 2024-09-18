from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        x_axis = randint(-280, 280)
        y_axis = randint(-280, 280)
        self.goto(x_axis, y_axis)

    def new_location(self):
        x_axis = randint(-280, 280)
        y_axis = randint(-280, 280)
        self.goto(x_axis, y_axis)


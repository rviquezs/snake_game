from tkinter.constants import RIGHT
from turtle import Turtle

from dns.update import UPDATE
from selenium.webdriver.common.devtools.v85.page import DownloadProgress

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
SPEED = 20
COLOR = 'white'
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color(COLOR)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_axis = self.segments[seg - 1].xcor()
            y_axis = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_axis, y_axis)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

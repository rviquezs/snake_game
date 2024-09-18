from turtle import Turtle

ALIGNMENT = 'center'
COLOR = 'white'
FONT = 'Courier'
FONT_SIZE = 15
FONT_TYPE = 'bold'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, FONT_TYPE))
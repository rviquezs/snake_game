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
        self.highest_score = int(self.get_highest_score())
        self.color(COLOR)
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def get_highest_score(self):
        with open('data.txt', mode='r') as data:
            self.highest_score = data.read()
        return self.highest_score

    def set_highest_score(self, score):
        with open('data.txt', mode='w') as data:
            data.write(str(score))
        self.highest_score = score

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  Record: {self.highest_score}", False, align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highest_score:
            self.set_highest_score(self.score)

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT,
    #                font=(FONT, FONT_SIZE, FONT_TYPE))
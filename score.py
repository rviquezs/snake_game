from turtle import Turtle
import json
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for both dev and PyInstaller bundles. """
    if hasattr(sys, '_MEIPASS'):
        # If running from a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # If running in normal Python environment
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

config_file_path = resource_path('config.json')
data_file_path = resource_path('assets/data.txt')

with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

COLOR = config["SCORE_COLOR"]
ALIGNMENT = config["SCORE_ALIGNMENT"]
FONT = config["SCORE_FONT"]
FONT_SIZE = config["SCORE_FONT_SIZE"]
FONT_TYPE = config["SCORE_FONT_TYPE"]


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
        with open(data_file_path, mode='r') as data:
            self.highest_score = data.read()
        return self.highest_score

    def set_highest_score(self, score):
        with open(data_file_path, mode='w') as data:
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
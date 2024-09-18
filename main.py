import time
from turtle import Screen
from snake import Snake

snake = Snake()

screen = Screen()
screen.setup(height=600, width=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

screen.exitonclick()

import time
from turtle import Screen
from snake import Snake

snake = Snake()
food = Food()
score = Score()

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

    # Detect collision food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        score.increase_score()

    # Detect collision walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()

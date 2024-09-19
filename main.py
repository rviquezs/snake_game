import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

def main():
    snake = Snake()
    food = Food()
    score = Score()

    screen = Screen()
    screen.setup(height=700, width=600)
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
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
            score.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()

    screen.exitonclick()

if __name__ == "__main__":
    main()

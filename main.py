from Food import Food
from Score import Score
from Snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.create_food()
        score.increase_score()
        snake.increase_length()

    head = snake.segments[0]

    for segment in snake.segments[1:]:
        if head.distance(segment) < 10:
            score.reset()
            snake.reset()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mo1der Snake Game")
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 35:
        food.refresh()
        snake.extend_snake()
        score.update_score()

    if snake.head.xcor() == 280 or snake.head.xcor() == -280 or snake.head.ycor() == 280 or snake.head.ycor() == -280:
        score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
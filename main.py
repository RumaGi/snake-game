from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

# Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detecting collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

        # scoreboard.game_over()
        # game_on = False

# Detecting collision with tail
    for segment in snake.segments[1:]:   # LOOPING EVERY OTHER SEGMENT OTHER THAN THE FIRST SEGMENT WHICH IS THE HEAD
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

            # scoreboard.game_over()
            # game_on = False






screen.exitonclick()
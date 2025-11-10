from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("MOBY'S SNAKEO")

def move():
    snake.move_snake()
    screen.update()
    time.sleep(0.15)

def grow():
    screen.tracer(0)
    snake.grow()

game = True
snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.east, "Right")
screen.onkey(snake.north, "Up")
screen.onkey(snake.west, "Left")
screen.onkey(snake.south, "Down")

snake.create_snake()

while game is True:
    restart = False
    move()
    if snake.head.distance(food) < 15:
        food.relocate()
        score.score_up()
        grow()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        restart = True

    for part in snake.full_snake[1:]:
        if snake.head.distance(part) < 10:
           restart = True

    if restart is True:
        snake.restart()
        score.reset_score()

screen.exitonclick()
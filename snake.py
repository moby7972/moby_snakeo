from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class Snake:
    def __init__(self):
        self.full_snake = []
        self.head = Turtle()
        self.x_axis = 0
        self.current_color = "N/A"

    def add_part(self):
        snake = Turtle("square")
        snake.color("black")
        snake.penup()
        snake.setpos(x=self.x_axis, y=0)
        self.x_axis -= DISTANCE
        self.full_snake.append(snake)
        color = random.choice(COLORS)
        while color == self.current_color:
            color = random.choice(COLORS)
        snake.color(color)
        self.current_color = color

    def create_snake(self):
        for i in range(3):
            self.add_part()
        self.head = self.full_snake[0]

    def restart(self):
        for part in self.full_snake:
            part.hideturtle()
        self.__init__()
        self.create_snake()

    def sort_snake(self):
        j = len(self.full_snake)
        while j > 0:
            for i in range(j - 1):
                temp = self.full_snake[i]
                self.full_snake[i] = self.full_snake[i + 1]
                self.full_snake[i + 1] = temp
            j -= 1

    def move_snake(self):
        self.sort_snake()
        for part_num in range(len(self.full_snake) - 1):
            new_x = self.full_snake[part_num + 1].xcor()
            new_y = self.full_snake[part_num + 1].ycor()
            self.full_snake[part_num].goto(new_x, new_y)
        self.full_snake[len(self.full_snake) - 1].forward(DISTANCE)
        self.sort_snake()

    def grow(self):
        self.add_part()

    def east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)


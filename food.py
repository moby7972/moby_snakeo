from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.relocate()

    def relocate(self):
        self.goto(random.randint(-200, 200), random.randint(-200, 200))

from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.clear()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5)
        position = [random.randint(-280, 280), random.randint(-280, 280)]
        self.setposition(position[0], position[1])

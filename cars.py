"""This file will control the cars."""
import turtle
from random import randrange

# Make a constant to specify the x position the cars will be:
CAR_X = 300


class Cars:
    """This class will control the cars."""

    def __init__(self):
        """Sets the car speed."""
        self.speed = 1
        self.cars = []

    def car(self):
        """Makes a car with a random color and a random y position."""
        t = turtle.Turtle("square")
        t.shapesize(stretch_wid=1, stretch_len=3)
        t.penup()

        turtle.colormode(255)
        r = randrange(start=100, stop=201)
        b = randrange(start=100, stop=201)
        g = randrange(start=100, stop=201)
        t.color((r, g, b))

        car_y = randrange(start=-160, stop=241, step=20)
        t.goto((CAR_X, car_y))
        self.cars.append(t)

    def move(self):
        """Moves all the cars towards the left."""
        for i in self.cars:
            i.goto((i.xcor() - 10, i.ycor()))

    def reset(self):
        """Clear all the cars."""
        for i in self.cars:
            i.hideturtle()
        self.cars = []

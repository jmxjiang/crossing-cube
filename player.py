"""This file controls the player."""
from turtle import Turtle

# Make a constant for the restart position:
STARTING = (0, -200)


class Player(Turtle):
    """Controls the player."""

    def __init__(self):
        """Sets the player into the starting position"""
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.restart()

    def restart(self):
        """Sets the player back into the starting position for a new level."""
        self.goto(STARTING)

    def up(self):
        """Moves the turtle forward."""
        self.forward(10)

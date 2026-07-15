"""This file will control the level the player is on."""
from turtle import Turtle

# Make a constant for the font:
FONT = ("Arial", 20, "normal")

# Make a constant for the cords of the level display:
POSITION = (-270, 270)


class Level(Turtle):
    """This class controls the level."""
    def __init__(self):
        """Sets the level to 1."""
        super().__init__()
        self.level = 0
        self.level_up()

    def level_up(self):
        """Increases the level by one."""
        self.level += 1
        self.clear()
        self.penup()
        self.goto(POSITION)
        self.write(arg=f"Level {self.level}", font=FONT)
        self.hideturtle()

    def end(self):
        """Ends the game."""
        self.clear()
        self.goto(POSITION)
        self.write(arg=f"Game over. Your score was {self.level}.", font=FONT)
        self.hideturtle()

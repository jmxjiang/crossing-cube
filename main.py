"""This file will control how the game works by using the other classes."""
from turtle import Screen
from level import Level
from time import sleep
from player import Player
from cars import Cars

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Set the level to 1:
level = Level()

# Set up the player:
player = Player()
screen.onkey(fun=player.up, key="w")

# Set up the cars
cars = Cars()

# Have a loop to keep running the game until its over:
game_is_on = True
counter = 0
while game_is_on:
    # Check if the player is touching a car:
    for i in cars.cars:
        if (player.distance(i) < 20 or (player.xcor() in range(i.xcor() - 30, i.xcor() + 31) and
                                        player.ycor() in range(i.ycor() - 10, i.ycor() + 11))):
            game_is_on = False
            level.end()
            break

    if game_is_on:
        counter += cars.speed
        # If the player reaches the end, go to the next level:
        if player.ycor() > 280:
            level.level_up()
            cars.reset()
            player.restart()
            cars.speed += 1

        # Make a car when time is up:
        if counter >= 10:
            counter = 0
            cars.car()

        # Make the cars go faster at a certain level
        if level.level >= 10:
            sleep(0.03)
        elif level.level >= 6:
            sleep(0.5 / level.level)
        else:
            sleep(0.1)

        cars.move()
        screen.update()

screen.exitonclick()

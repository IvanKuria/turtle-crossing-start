from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.origin()

    # this controls the movement of the turtle
    def go_up(self):
        self.forward(10)

    # Returns the player to the start
    def origin(self):
        self.goto(STARTING_POSITION)


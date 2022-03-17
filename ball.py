from random import choice
from turtle import Turtle

MOVE_DISTANCE = 20
START_RIGHT = [45, 315]
START_LEFT = [135, 225]
MOVE_RIGHT_UP = 45
MOVE_RIGHT_DOWN = 315
MOVE_LEFT_UP = 135
MOVE_LEFT_DOWN = 225
STARTING_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.seth(choice(START_RIGHT))
        # TODO self.seth(-315)
        self.penup()
        self.move_speed = STARTING_SPEED

    def move(self):
        self.forward(MOVE_DISTANCE)

    # TODO Check if there's not a way to do a single bounce with negative heading
    def bounce_wall(self):
        if self.heading() == MOVE_RIGHT_UP:
            self.seth(MOVE_RIGHT_DOWN)
        elif self.heading() == MOVE_LEFT_UP:
            self.seth(MOVE_LEFT_DOWN)
        elif self.heading() == MOVE_RIGHT_DOWN:
            self.seth(MOVE_RIGHT_UP)
        else:
            self.seth(MOVE_LEFT_UP)

    def bounce_paddle(self):
        if self.heading() == MOVE_RIGHT_UP:
            self.seth(MOVE_LEFT_UP)
        elif self.heading() == MOVE_LEFT_UP:
            self.seth(MOVE_RIGHT_UP)
        elif self.heading() == MOVE_RIGHT_DOWN:
            self.seth(MOVE_LEFT_DOWN)
        else:
            self.seth(MOVE_RIGHT_DOWN)
        self.move_speed *= 0.9

    def to_right(self):
        self.home()
        self.move_speed = STARTING_SPEED
        self.seth(choice(START_RIGHT))

    def to_left(self):
        self.home()
        self.move_speed = STARTING_SPEED
        self.seth(choice(START_LEFT))



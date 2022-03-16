from turtle import Turtle

MOVE_DISTANCE = 20
MOVE_START = 45
MOVE_BOUNCE = 180


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.seth(MOVE_START)
        self.penup()

    def move(self):
        self.forward(MOVE_DISTANCE)

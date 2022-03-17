from turtle import Turtle

RIGHT = 350
LEFT = -350
Y_START_POSITION = 0
PADDLE_LENGTH = 100 / 20
MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_LENGTH, stretch_len=1)
        self.penup()
        self.setposition(side, Y_START_POSITION)

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle, LEFT, RIGHT

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle(RIGHT)
left_paddle = Paddle(LEFT)
ball = Ball()

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="s")
screen.onkey(fun=left_paddle.move_down, key="w")

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(0.2)

screen.exitonclick()


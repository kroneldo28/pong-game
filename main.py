import time
from turtle import Screen

from ball import Ball
from paddle import Paddle, LEFT, RIGHT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle(RIGHT)
left_paddle = Paddle(LEFT)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="s")
screen.onkey(fun=left_paddle.move_down, key="w")

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collisions with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collisions with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # Detect when th ball is missed
    # Right paddle misses
    if ball.xcor() > 390:
        scoreboard.point_left()
        ball.to_left()
    # Left paddle misses
    if ball.xcor() < -390:
        scoreboard.point_right()
        ball.to_right()

    # The game ends as soon as one player reach 10 points
    if scoreboard.right_score == 10 or scoreboard.left_score == 10:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()


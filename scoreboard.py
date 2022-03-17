from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 88, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 88, "normal"))

    def point_left(self):
        self.left_score += 1
        self.update_scoreboard()

    def point_right(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align="center", font=("Courier", 88, "normal"))


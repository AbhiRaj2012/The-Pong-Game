from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
import turtle


class Boundary:
    def __init__(self):
        self.wall_turtle = turtle.Turtle()
        self.wall_turtle.color('Dodgerblue4')
        self.wall_turtle.hideturtle()
        self.wall_turtle.penup()
        self.wall_turtle.pensize(5)
        self.draw_board()


    def draw_board(self):
        self.wall_turtle.goto(-400, -300)
        self.wall_turtle.pendown()
        for _ in range(2):
            self.wall_turtle.forward(800)
            self.wall_turtle.left(90)
            self.wall_turtle.forward(600)
            self.wall_turtle.left(90)

        self.wall_turtle.penup()
        self.wall_turtle.goto(0, 300)
        self.wall_turtle.pendown()
        self.wall_turtle.setheading(270)
        self.wall_turtle.forward(600)

        self.wall_turtle.goto(0, -100)
        self.wall_turtle.setheading(0)
        self.wall_turtle.circle(100)
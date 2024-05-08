import time
import turtle
import base
import paddles
import ball
import scoreboard

LEFT = (370, 0)
RIGHT = (-370, 0)

screen = turtle.Screen()
screen.bgcolor("Dodgerblue2")
screen.setup(900, 700)
screen.title("The Pong Game")
screen.tracer(0)

boundary = base.Boundary()
left_paddle = paddles.Paddle(LEFT)
right_paddle = paddles.Paddle(RIGHT)
game_Ball = ball.Ball()
score = scoreboard.ScoreBoard()

screen.listen()

screen.onkey(left_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'Up')

screen.onkey(right_paddle.go_up, 'w')
screen.onkey(right_paddle.go_down, 's')

run = True
while run:
    time.sleep(game_Ball.motion_interval)
    screen.update()
    game_Ball.move()

    # detecting the collision with upper and lower wall
    if game_Ball.ycor() > 280 or game_Ball.ycor() < -280:
        game_Ball.bounce_y()

    if game_Ball.distance(left_paddle) < 50 and game_Ball.xcor() > 340 or game_Ball.distance(
            right_paddle) < 50 and game_Ball.xcor() < -340:
        game_Ball.bounce_x()

    # detecting when L paddle misses the ball
    if game_Ball.xcor() > 380:
        game_Ball.reset_position()
        score.r_point()

    # detecting when R paddle misses the ball
    if game_Ball.xcor() < -380:
        game_Ball.reset_position()
        score.l_point()

screen.exitonclick()

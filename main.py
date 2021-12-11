import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import ScoreBoard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# Screen Settings
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("blue")
screen.tracer(0)
screen.listen()

# Score Board
score = ScoreBoard()

# Left Paddle and Control Paddle
paddleLeft = Paddle(-380)
screen.onkey(paddleLeft.Up, "w")
screen.onkey(paddleLeft.Down, "s")

# Right Paddle
paddleRight = Paddle(380)
screen.onkey(paddleRight.Up, "Up")
screen.onkey(paddleRight.Down, "Down")

# Wall
wall = Wall()

# Ball
ball = Ball()

condition = True
while condition:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # Ball Wall
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounceY()

    # Detect Collision with paddle
    print(ball.xcor())
    if (ball.distance(paddleRight) < 50 and ball.xcor() > 350) or (ball.distance(paddleLeft) < 50 and ball.xcor() < -350):
        ball.bounceX()

    # Point Right
    if ball.xcor() > 380:
        score.increaseLeft()
        ball.resetBall()

    # Point Left
    if ball.xcor() < -390:
        score.increaseRight()
        ball.resetBall()


screen.exitonclick()

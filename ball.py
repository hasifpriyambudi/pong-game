from turtle import Turtle
import random

FIRST_MOVE = [10, -10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xMove = random.choice(FIRST_MOVE)
        self.yMove = random.choice(FIRST_MOVE)
        self.moveSpeed = 0.1

    def move(self):
        self.goto(self.xcor()+self.xMove, self.ycor()+self.yMove)

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1
        self.moveSpeed *= 0.9

    def resetBall(self):
        self.moveSpeed = 0.1
        self.goto(0, 0)

    def increaseSpeed(self):
        self.speed(self.speed()+3)
        print(self.speed())

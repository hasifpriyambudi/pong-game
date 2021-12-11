from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.scoreBoard()

    def scoreBoard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(self.rightScore, align="center", font=("Arial", 24, "normal"))

    def increaseLeft(self):
        self.leftScore += 1
        self.scoreBoard()

    def increaseRight(self):
        self.rightScore += 1
        self.scoreBoard()

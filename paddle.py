from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, yPos):
        super().__init__()
        self.yPos = yPos
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.setpos(self.yPos, 0)

    def Up(self):
        if self.ycor() < 200:
            self.goto(self.yPos, self.ycor()+20)

    def Down(self):
        if self.ycor() > -200:
            self.goto(self.yPos, self.ycor()-20)

from turtle import Turtle


class Wall:
    def __init__(self):
        self.walls = []
        self.createWallTop()
        self.createWallBottom()

    def createWallTop(self):
        y = 260
        x = -400
        for i in range(40):
            wall = Turtle("square")
            wall.penup()
            wall.color("pink")
            wall.setpos(x, y)
            x += 20
            self.walls.append(wall)

    def createWallBottom(self):
        y = -255
        x = -400
        for i in range(40):
            wall = Turtle("square")
            wall.penup()
            wall.color("pink")
            wall.setpos(x, y)
            x += 20
            self.walls.append(wall)

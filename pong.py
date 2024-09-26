import turtle

STARTING_POSITION = []


class Pong:
    def __init__(self):
        self.paddlelist = []
        self.create()
        self.position()

    def create(self):
        for i in range(2):
            paddle = turtle.Turtle("square")
            paddle.color("white")
            paddle.speed("fastest")
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.penup()
            self.paddlelist.append(paddle)

    def position(self):
        self.paddlelist[0].goto(380, 0)
        self.paddlelist[1].goto(-390, 0)

    def move_up_r(self):
        new_y = self.paddlelist[0].ycor() + 20
        self.paddlelist[0].goto(self.paddlelist[0].xcor(), new_y)

    def move_down_r(self):
        new_y = self.paddlelist[0].ycor() - 20
        self.paddlelist[0].goto(self.paddlelist[0].xcor(), new_y)

    def move_up_l(self):
        new_y = self.paddlelist[1].ycor() + 20
        self.paddlelist[1].goto(self.paddlelist[1].xcor() , new_y)

    def move_down_l(self):
        new_y =  self.paddlelist[1].ycor() - 20
        self.paddlelist[1].goto(self.paddlelist[1].xcor() , new_y)

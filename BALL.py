from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_move = 10
        self.x_move = 10
        self.create()
        self.fast = 0.10

    def create(self):
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def left_paddle_collision(self):
        self.x_move *= -1
        if self.fast > 0:
            self.fast -= 0.01

    def right_paddle_collision(self):
        self.x_move *= -1
        if self.fast > 0:
            self.fast -= 0.01

    def reset_position(self):
        self.x_move *= -1
        self.fast = 0.1
        self.goto(0,0)

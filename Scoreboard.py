import turtle

SCORE_POSITION = [(100, 250), (-100, 250)]


class ScoreBoard:
    def __init__(self):
        self.line()
        self.scorelist = []
        self.left_score = 0
        self.right_score = 0
        self.score()

    def line(self):
        line = turtle.Turtle()
        line.penup()
        line.goto(0, 300)
        line.color("white")
        line.pendown()
        line.goto(0, -300)

    def score(self):
        for i in range(2):
            sc = turtle.Turtle()
            sc.penup()
            sc.color("white")
            sc.hideturtle()
            sc.goto(SCORE_POSITION[i])
            sc.write(self.right_score, align="center", font=("Courier", 30, "normal"))
            self.scorelist.append(sc)

    def l_point(self):
        self.scorelist[1].clear()
        self.left_score  += 1
        self.scorelist[1].write(self.left_score, align="center", font=("Courier", 30, "normal"))

    def r_point(self):
        self.scorelist[0].clear()
        self.right_score += 1
        self.scorelist[0].write(self.right_score, align="center", font=("Courier", 30, "normal"))

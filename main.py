import turtle
import pong
import time
import BALL
import Scoreboard


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(height=600, width=800)
screen.tracer(0)

p = pong.Pong()
ball = BALL.Ball()
sb = Scoreboard.ScoreBoard()

screen.listen()
screen.onkeypress(p.move_up_r, "Up")
screen.onkeypress(p.move_down_r, "Down")
screen.onkeypress(p.move_up_l, "w")
screen.onkeypress(p.move_down_l, "s")

game = True
while game:
    screen.update()
    time.sleep(ball.fast)
    ball.move()

    # detecting ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(p.paddlelist[0]) < 40 and ball.xcor() > 350:
        ball.right_paddle_collision()

    if ball.distance(p.paddlelist[1]) < 40 and ball.xcor() < -350:
        ball.left_paddle_collision()

    # when ball goes out of right screen
    if ball.xcor() > 400:
        sb.l_point()
        ball.reset_position()

    # when ball goes out of left screen
    if ball.xcor() < -400:
        sb.r_point()
        ball.reset_position()

screen.exitonclick()

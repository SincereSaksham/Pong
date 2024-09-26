import turtle

turtle.bgcolor("black")

timmy = turtle.Turtle()
timmy.speed(70)
timmy.hideturtle()
timmy.pencolor("purple")
for i in range(10000):
    timmy.forward(i)
    timmy.left(91)

import turtle

wn = turtle.Screen()
wn.title("Ping Pong Game By Frnzy")
wn.bgcolor("black")
wn.setup(width=1000, height=700)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("aqua")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("aqua")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)


# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 4.3
ball.dy = 4.3


# Functions to move paddles
def paddle_a_up():
    if paddle_a.ycor() < 300:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() > -300:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() < 300:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() > -300:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


# KeyBoard Key for Calling the functions
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main Game Loop Every Frame Gets Updated
while True:
    wn.update()
    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() - ball.dy)

    # Border
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1  # reverse the direction of ball

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1  # reverse the direction of ball

    if ball.xcor() >= 490:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() <= -490:
        ball.goto(0, 0)
        ball.dx *= -1

    # Collision Detection
    if ball.xcor() < -445 and abs(ball.ycor() - paddle_a.ycor()) < 50:
        ball.setx(-440)
        ball.dx *= -1
    if ball.xcor() > 445 and abs(ball.ycor() - paddle_b.ycor()) < 50:
        ball.setx(440)
        ball.dx *= -1

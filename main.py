from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# left and right Paddle
l_paddle = Paddle((-435,0))
r_paddle = Paddle((425,0))

# bouncing ball
ball = Ball()
ball.move()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Adjust sleep time for smoother gameplay
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 405 or ball.distance(l_paddle) < 50 and ball.xcor() < -415:
        ball.bounce_x()

    # Detect when the ball goes out of bounds
    if ball.xcor() > 450:
        # Reset the ball or give a point to the left player
        scoreboard.l_point()
        ball.reset_position()
    elif ball.xcor() < -450:
        # Reset the ball or give a point to the right player
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()

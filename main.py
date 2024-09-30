from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# left and right Paddle
l_paddle = Paddle((-430,0))
r_paddle = Paddle((420,0))

# bouncing ball
ball = Ball()
ball.move()




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()

    

screen.exitonclick()
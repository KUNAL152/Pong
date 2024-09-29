from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle_left = Turtle("square")
paddle_left.color = "white"
paddle_left.goto = (0,0)



screen.exitonclick()
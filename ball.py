from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.penup()

    def move(self):
        new_x = self.ball.xcor()+10
        new_y = self.ball.ycor()+10
        self.ball.goto(new_x,new_y)

from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_len=1,stretch_wid=4)
        self.paddle.penup()
        self.paddle.goto(pos)

    def go_up(self):
        new_Y = self.paddle.ycor()+20
        self.paddle.goto(self.paddle.xcor(), new_Y)

    def go_down(self):
        new_Y = self.paddle.ycor()-20
        self.paddle.goto(self.paddle.xcor(), new_Y)
        
        
    





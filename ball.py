from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.screen.update()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove = -self.ymove

    def paddle_bounce(self):
        self.xmove = -self.xmove
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.paddle_bounce()
        
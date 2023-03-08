from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.speed("fastest")
        self.setheading(90)
        self.screen.update()

    def up(self):
        if self.heading() != 90:
            self.setheading(90)
        self.forward(20)

    def down(self):
        if self.heading() != 270:
            self.setheading(270)
        self.forward(20)


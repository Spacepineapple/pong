from turtle import Turtle
FONT = ("Courier", 18, "normal")
coordinate = (0, 270)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color("white")
        self.penup()
        self.goto(coordinate)
        self.write(f"Score: {self.score_1} {self.score_2}", False, align="center", font=FONT)
        self.hideturtle()

    def increase_score(self, player):
        if player == 1:
            self.score_1 +=1
        elif player == 2:
            self.score_2 +=1
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score_1} {self.score_2}", False, align="center", font=FONT)



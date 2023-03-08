from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
timmy = Turtle()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle()
player_2 = Paddle()
ball = Ball()
score = Score()
sleep = 0.05

player_1.goto(-350,0)
player_2.goto(350,0)
ball.goto(0,0)

playing = True
screen.listen()
screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")


while playing:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < - 320:
        ball.paddle_bounce()
        if ball.move_speed>0.02:
            ball.move_speed-=0.01
    elif ball.xcor() > 380:
        score.increase_score(1)
        ball.reset()
    elif ball.xcor() <-380:
        score.increase_score(2)
        ball.reset()
            

screen.exitonclick()
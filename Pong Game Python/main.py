from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title = "Ping Pong"
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect colision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall ()
        
    # Detect colision with paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50) :
        ball.bounce_paddle()
    
    # When R paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # When L paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick() 
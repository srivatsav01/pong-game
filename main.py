from turtle import Turtle, Screen
from my_board import MyBoard
from ball import Ball
import time
from scores import  Score


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
my_board = MyBoard()
my_board.goto(350,0)
other_board = MyBoard()
other_board.goto(-350,0)
screen.listen()
screen.onkey(my_board.up,"Up")
screen.onkey(my_board.down,"Down")

screen.onkey(other_board.up,"w")
screen.onkey(other_board.down,"s")

design = Turtle()
design.color("white")
design.hideturtle()
design.left(90)
for i in range(10):
    design.pendown()
    design.forward(20)
    design.penup()
    design.forward(10)
design.goto(0,0)
design.left(180)
for i in range(10):
    design.pendown()
    design.forward(20)
    design.penup()
    design.forward(10)



#Ball
ball =Ball()
game_is_on = True


#ball in play
ball_in_play = ball
ball_in_play.speed("fastest")

# score board
score = Score()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball_in_play.move()
    #collisions with wall
    x_cor = ball_in_play.xcor()
    y_cor = ball_in_play.ycor()
    if y_cor > 280 or y_cor < -280:
        ball_in_play.bounce_y()

    #collisions with paddle
    distance_1_xcor= abs(my_board.xcor() - ball_in_play.xcor())
    distance_1_ycor= abs(my_board.ycor() - ball_in_play.ycor())
    distance_2_xcor = abs(other_board.xcor() - ball_in_play.xcor())
    distance_2_ycor = abs(other_board.ycor() - ball_in_play.ycor())

    if (distance_1_xcor < 10 and distance_1_ycor < 50) or (distance_2_xcor < 10 and distance_2_ycor < 50):
       ball_in_play.bounce_y()
       ball_in_play.bounce_x()

    if ball_in_play.xcor() > 400 :
        time.sleep(1)
        new_ball = Ball()
        ball_in_play = new_ball
        ball_in_play.bounce_x()
        score.others_point()
        other_board.goto(-350,0)
        my_board.goto(350,0)
    if ball_in_play.xcor() < -400:
        new_ball = Ball()

        ball_in_play = new_ball
        score.my_poinnt()
        time.sleep(1)
        other_board.goto(-350, 0)
        my_board.goto(350, 0)
    if score.my_score >9 or score.others_score > 9:
        game_is_on = False























screen.exitonclick()
from turtle import  Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.others_score = 0
        self.my_score = 0
        self.penup()
        self.hideturtle()
        self.goto(-100,200)
        self.write(self.others_score,align="center", font =("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.my_score,align="center", font =("Courier", 80, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.others_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.my_score, align="center", font=("Courier", 80, "normal"))

    def others_point(self):
        self.others_score += 1
        self.update_score()

    def my_poinnt(self):
        self.my_score += 1
        self.update_score()
    def game_over(self):
        self.clear()
        self.update_score()


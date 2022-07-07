from turtle import Turtle
STARTING_POSITIONS = [(350,30),(350,15),(350,0)]

class MyBoard(Turtle):
    def __init__(self):
      super().__init__()
      self.shape("square")
      self.penup()
      self.color("white")
      self.shapesize(stretch_len=5)
      self.setheading(90)
      self.speed("fastest")

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

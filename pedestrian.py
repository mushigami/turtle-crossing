from turtle import Turtle

STEP_SIZE = 10


class Pedestrian(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        self.goto(self.xcor(), self.ycor() + STEP_SIZE)

    def reset_position(self):
        self.goto(0, -250)


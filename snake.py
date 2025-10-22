from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            segx = self.segments[i - 1].xcor()
            segy = self.segments[i - 1].ycor()
            self.segments[i].goto(segx, segy)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def create(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
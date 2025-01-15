from turtle import Turtle

move_distance = 20


start_position = [(0, 0), (-20, 0), (-40, 0)]

# for customizing starting points


class Snake:

    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]        # storing the head in a variable fro acsessbility

    def make_snake(self):
        for position in start_position:  # for position in start_position:
            self.add_segment(position)  # creating the f

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)       # position is the variable for starting co-ordinates
        self.segments.append(segment)  # add the created segments to "segments" list

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()   # all segments are removed from previous game
        self.make_snake()       # new 3 segments snake is created
        self.head = self.segments[0]  # head to be 0th item in the segments list

    def extend(self):
        # adding a segment at the end of the list
        # when snake eats food adding a segment in the same position
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):    # if 5 heads,from 4 to  1
            new_x = self.segments[segment_number - 1].xcor()    # getting x cor from the segment ahead of them
            new_y = self.segments[segment_number - 1].ycor()    # same as above for y cor
            self.segments[segment_number].goto(new_x, new_y)    # sending the segment to position of segment in front
        self.head.forward(move_distance)   # sending the snake's head that is the first head 20paces forward

    # heading 270(down), 90(up) , 0(right), 180(left)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self) :
        if self.head.heading() != 180:
            self.head.setheading(0)

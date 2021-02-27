import turtle as t

initial_position = [(0, 0), (-20, 0), (-40, 0)]



class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in initial_position:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_turtle = t.Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(pos)
        self.segments.append(new_turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)
        if self.segments[0].xcor() > 300:
            y_cor = self.segments[0].ycor()
            self.segments[0].setposition(-300, y_cor)
        if self.segments[0].xcor() < -300:
            y_cor = self.segments[0].ycor()
            self.segments[0].setposition(300, y_cor)
        if self.segments[0].ycor() > 300:
            x_cor = self.segments[0].xcor()
            self.segments[0].setposition(x_cor, -300)
        if self.segments[0].ycor() < -300:
            x_cor = self.segments[0].xcor()
            self.segments[0].setposition(x_cor, 300)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def increase_length(self):
        new_turtle = t.Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_index_x = self.segments[-1].xcor()
        new_index_y = self.segments[-1].ycor()
        new_turtle.setposition(new_index_x, new_index_y)
        self.segments.append(new_turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
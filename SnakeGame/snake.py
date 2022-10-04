from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    x_pos = 0
    y_pos = 0
    position = (x_pos, y_pos)

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(self.position)
            new_segment.color("white")
            self.snake_segments.append(new_segment)
            self.x_pos -= 20

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(self.x_pos, self.y_pos)
        new_segment.color("white")
        self.snake_segments.append(new_segment)

        self.x_pos -= 20

    def extend_snake(self):
        pass

    def move(self):
        for seg_idx in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[seg_idx].goto(self.snake_segments[seg_idx - 1].pos())

        self.head.forward(MOVE_DISTANCE)
        # self.snake_segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

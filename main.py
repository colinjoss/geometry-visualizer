from svg_turtle import SvgTurtle
from turtle import *
from CONSTANTS import *
import math as m


class Geometry:
    def __init__(self):
        self.cursor = Turtle()
        if SVG:
            self.cursor = SvgTurtle(2500, 2500)
        self.cursor.speed(SPEED)
        self.cursor.width(THICKNESS)
        self.cursor.hideturtle()
        screensize(canvwidth=1080, canvheight=720)

        # BASIC SHAPE FUNCTIONS

    def circle(self, circumference, color=None):
        """Generates a circle of the given circumference."""
        if color:
            self.set_color(color)

        self.cursor.circle(circumference // 2, steps=360)
        self.cursor.end_fill()

    def triangle(self, length, color=None):
        """Generates a regular triangle of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(3):
            self.cursor.forward(length)
            self.cursor.left(360 / 3)
        self.cursor.end_fill()

    def golden_triangle(self, base_length, color=None):
        """Generates a golden triangle of the given base length."""
        if color:
            self.set_color(color)
        origin = self.cursor.pos()
        self.cursor.forward(base_length)
        self.cursor.left(108)
        self.cursor.forward(base_length * PHI)
        self.cursor.left(144)
        self.cursor.forward(base_length * PHI)
        self.cursor.left(108)
        self.move_to_coord(origin[0], origin[1])
        self.cursor.end_fill()

    def square(self, length, color=None):
        """Generates a square of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(360 / 4)
        self.cursor.end_fill()

    def rectangle(self, length, color=None):
        """Generates a rectangle of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(90)
            self.cursor.forward(length * 2)
            self.cursor.left(90)
        self.cursor.end_fill()

    def rhombus(self, length, angle, color=None):
        """Generates a parallelogram of the given length and height."""
        if color:
            self.set_color(color)

        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(angle)
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
        self.cursor.end_fill()

    def parallelogram(self, length, height, angle, color=None):
        """Generates a parallelogram of the given length and height."""
        if color:
            self.set_color(color)

        if angle == 90:
            print('Invalid angle parameter 90: use square function')
            return False

        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
            self.cursor.forward(height)
            self.cursor.left(angle)
        self.cursor.end_fill()

    def pentagon(self, length, color=None):
        """Generates a regular pentagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(5):
            self.cursor.forward(length)
            self.cursor.left(360 / 5)
        self.cursor.end_fill()

    def hexagon(self, length, color=None):
        """Generates a regular hexagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(6):
            self.cursor.forward(length)
            self.cursor.left(360 / 6)
        self.cursor.end_fill()

    def heptagon(self, length, color=None):
        """Generates a regular hexagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(7):
            self.cursor.forward(length)
            self.cursor.left(360 / 7)
        self.cursor.end_fill()

    def octagon(self, length, color=None):
        """Generates a regular octagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(8):
            self.cursor.forward(length)
            self.cursor.left(360 / 8)
        self.cursor.end_fill()

    def nonagon(self, length, color=None):
        """Generates a regular nonagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(9):
            self.cursor.forward(length)
            self.cursor.left(360 / 9)
        self.cursor.end_fill()

    def decagon(self, length, color=None):
        """Generates a regular decagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(10):
            self.cursor.forward(length)
            self.cursor.left(360 / 10)
        self.cursor.end_fill()

    def hendecagon(self, length, color=None):
        """Generates a regular hendecagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(11):
            self.cursor.forward(length)
            self.cursor.left(360 / 11)
        self.cursor.end_fill()

    def dodecagon(self, length, color=None):
        """Generates a regular dodecagon of the given side length."""
        if color:
            self.set_color(color)

        for _ in range(12):
            self.cursor.forward(length)
            self.cursor.left(360 / 12)
        self.cursor.end_fill()

    def n_agon(self, sides, length, color=None):
        """Generates a regular polygon of the given number of sides and side length."""
        if color:
            self.set_color(color)

        for _ in range(sides):
            self.cursor.forward(length)
            self.cursor.left(360 / sides)
        self.cursor.end_fill()

    def irregular_polygon(self, sides, lengths, angles, color=None):
        """Generates an irregular polygon of the given sides, lengths, and angles."""
        if color:
            self.set_color(color)

        for i in range(0, sides):
            self.cursor.forward(lengths[i])
            self.cursor.left(angles[i])
        self.cursor.end_fill()

    # MOVEMENT FUNCTIONS

    def move_to_coord(self, x, y) -> tuple:
        """Moves cursor to given coordinates and returns new coordinate as tuple."""
        self.cursor.penup()
        self.cursor.goto(x, y)
        self.cursor.pendown()
        return self.cursor.pos()

    # COLOR FUNCTIONS

    @staticmethod
    def valid_color_map(color_map):
        """Returns true if the color map is valid, otherwise returns false."""
        if color_map is None:
            return True
        elif not isinstance(color_map, list):
            print('Invalid color pattern parameter: must be list')
            return False
        if all(isinstance(x, tuple) for x in color_map) or all(isinstance(x, str) for x in color_map):
            return True
        print('Invalid color pattern parameter: inconsistent element types')
        return False

    @staticmethod
    def set_color_map(color_map, depth):
        """Interprets valid color map input and returns appropriately formatted color map."""
        # If color map is None, return array of (None, None)
        if color_map is None:
            return [(None, None) for _ in range(0, depth)]

        # If color map contains (pen, fill) tuple, extend pattern to length depth and return
        elif all(isinstance(x, tuple) for x in color_map):
            color_map = color_map * m.ceil(depth / len(color_map))
            return color_map[:depth]

        # If color map contains hex strings, interpret as (pen, fill) pair, extend pattern to length depth, and return
        elif all(isinstance(x, str) for x in color_map):
            color_map = [(color_map[i], color_map[i]) for i in range(0, len(color_map))]
            color_map = color_map * m.ceil(depth / len(color_map))
            print(color_map[:depth])
            return color_map[:depth]

    def set_color(self, color):
        """Takes color parameter and sets colors using Turtle functions."""
        if isinstance(color, str):
            self.cursor.pencolor(color)
            self.cursor.begin_fill()
            self.cursor.fillcolor(color)
        elif isinstance(color, tuple):
            if color[0]:
                self.cursor.pencolor(color[0])
            if color[1]:
                self.cursor.begin_fill()
                self.cursor.fillcolor(color[1])
        else:
            print('Invalid color parameter: not tuple')


if __name__ == '__main__':
    geo = Geometry()

    if SVG:
        geo.cursor.save_as('test.svg')
    else:
        done()

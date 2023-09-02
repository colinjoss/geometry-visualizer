from svg_turtle import SvgTurtle
from turtle import *
import math as m
import os
from matplotlib.colors import is_color_like
import inspect
from COLORS import *


SPEED = 'fastest'
THICKNESS = 5
PHI = 1.618033988749
DIAGONAL_CORRECTION = 0.70710678118

CIRCLE = "circle"
TRIANGLE = "triangle"
SQUARE = "square"
PENTAGON = "pentagon"
HEXAGON = "hexagon"
HEPTAGON = "heptagon"
OCTAGON = "octagon"
NONAGON = "nonagon"
DECAGON = "decagon"
HENDECAGON = "hendecagon"
DODECAGON = "dodecagon"

CONSTANT = "constant"
LOGARITHMIC = "logarithmic"


class Geometry:
    def __init__(self, line_thickness, export):
        self.cursor = Turtle()
        self.export_as_svg = False
        if export:
            self.cursor = SvgTurtle(1500, 1500)
            self.export_as_svg = True
        self.cursor.speed(SPEED)
        self.cursor.width(line_thickness)
        self.cursor.hideturtle()

        self.regular_polygons_name = {
            CIRCLE: self.circle,
            TRIANGLE: self.triangle,
            SQUARE: self.square,
            PENTAGON: self.pentagon,
            HEXAGON: self.hexagon,
            HEPTAGON: self.heptagon,
            OCTAGON: self.octagon,
            NONAGON: self.nonagon,
            DECAGON: self.decagon,
            HENDECAGON: self.hendecagon,
            DODECAGON: self.dodecagon
        }
        self.regular_polygons_num = {
            1: CIRCLE,
            3: TRIANGLE,
            4: SQUARE,
            5: PENTAGON,
            6: HEXAGON,
            7: HEPTAGON,
            8: OCTAGON,
            9: NONAGON,
            10: DECAGON,
            11: HENDECAGON,
            12: DODECAGON
        }

        screensize(canvwidth=1080, canvheight=720)

    # BASIC SHAPES

    @filename
    def circle(self, circumference, color=None):
        """Draws a circle of the given circumference."""
        if self.valid_color(color):
            self.start_color(color)
        self.cursor.circle(circumference // 2, steps=360)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def triangle(self, length, color=None):
        """Draws a regular triangle of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(3):
            self.cursor.forward(length)
            self.cursor.left(360 / 3)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def golden_triangle(self, base_length, color=None):
        """Draws a golden triangle of the given base length."""
        if self.valid_color(color):
            self.start_color(color)
        origin = self.cursor.pos()
        self.cursor.forward(base_length)
        self.cursor.left(108)
        self.cursor.forward(base_length * PHI)
        self.cursor.left(144)
        self.cursor.forward(base_length * PHI)
        self.cursor.left(108)
        self.move_to_coord(origin[0], origin[1])
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def square(self, length, color=None):
        """Draws a square of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(360 / 4)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def rectangle(self, length, color=None, export=False):
        """Draws a rectangle of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(90)
            self.cursor.forward(length * 2)
            self.cursor.left(90)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def rhombus(self, length, angle, color=None):
        """Draws a parallelogram of the given length and height."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(angle)
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def parallelogram(self, length, height, angle, color=None):
        """Draws a parallelogram of the given length and height."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
            self.cursor.forward(height)
            self.cursor.left(angle)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def pentagon(self, length, color=None):
        """Draws a regular pentagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(5):
            self.cursor.forward(length)
            self.cursor.left(360 / 5)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def hexagon(self, length, color=None):
        """Draws a regular hexagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(6):
            self.cursor.forward(length)
            self.cursor.left(360 / 6)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def heptagon(self, length, color=None):
        """Draws a regular hexagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(7):
            self.cursor.forward(length)
            self.cursor.left(360 / 7)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def octagon(self, length, color=None):
        """Draws a regular octagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(8):
            self.cursor.forward(length)
            self.cursor.left(360 / 8)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def nonagon(self, length, color=None):
        """Draws a regular nonagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(9):
            self.cursor.forward(length)
            self.cursor.left(360 / 9)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def decagon(self, length, color=None):
        """Draws a regular decagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(10):
            self.cursor.forward(length)
            self.cursor.left(360 / 10)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def hendecagon(self, length, color=None):
        """Draws a regular hendecagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(11):
            self.cursor.forward(length)
            self.cursor.left(360 / 11)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def dodecagon(self, length, color=None):
        """Draws a regular dodecagon of the given side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(12):
            self.cursor.forward(length)
            self.cursor.left(360 / 12)
        self.cursor.end_fill()
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @filename
    def n_agon(self, sides, length, color=None):
        """Draws a regular polygon of the given number of sides and side length."""
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(sides):
            self.cursor.forward(length)
            self.cursor.left(360 / sides)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def irregular_polygon(self, sides, lengths, angles, color=None):
        """Draws an irregular polygon of the given sides, lengths, and angles."""
        if self.valid_color(color):
            self.start_color(color)
        for i in range(0, sides):
            self.cursor.forward(lengths[i])
            self.cursor.left(angles[i])
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def yin_yang(self):
        self.cursor.circle(100, 180)
        self.cursor.circle(50, 180)
        self.cursor.circle(-50, 180)
        self.cursor.circle(-100, 180)
        return inspect.stack()[0][3]

    @filename
    def bulb(self, size, depth):
        heading = 0
        for _ in range(depth):
            heading += 360 // depth
            self.cursor.circle(size, 90)
            self.cursor.left(90)
            self.cursor.circle(size, 90)
            self.cursor.setheading(heading)
        return inspect.stack()[0][3]

    # PATTERNS

    @filename
    def xness_from_yness(self, length, x, y, color_map=None):
        """Draws a regular polygon of side length x by wrapping it in regular polygons of side length y."""
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, x)
        if x < 3 or y < 3:
            print("Polygon error: Must have a side length of 3 or more")
            return False
        angle = 360 / x  # angle of rotation for y-shape
        for i in range(0, x):
            self.regular_polygons_num[y-3](length, color_map[i])
            self.cursor.forward(length)
            self.cursor.right(angle)
        return inspect.stack()[0][3]

    @filename
    def flower(self, polygon, size, depth, color_map=None, angle=0, spacing=0):
        """Draws the given regular polygon in a seed of life formation."""
        color_map = self.set_color_map(color_map, depth)
        for i in range(0, depth):
            self.move_left(angle, spacing)
            self.regular_polygons_name[polygon](size, color_map[i])
            self.cursor.left(360 / depth)
        return inspect.stack()[0][3]

    @filename
    def clover(self, size, depth, color=None):
        """Draws a clover pattern with the given number of petals."""
        if self.valid_color:
            self.start_color(color)
        angle = 360 / depth
        for _ in range(depth):
            self.cursor.circle(size // 2, steps=360, extent=angle*2)
            self.cursor.left(360-angle)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def shrink(self, polygon, size, depth, growth, rate, horizontal_centered=False, vertical_centered=False, color_map=None):
        """Draws given shape in overlapping growth pattern."""
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, depth)
        origin = self.cursor.pos()
        for i in range(0, depth):
            self.regular_polygons_name[polygon](size, color_map[i])
            if growth == CONSTANT:  # 1.2 hexagon
                if horizontal_centered:
                    origin = self.move_to_coord(origin[0] + (size - (size - rate)) // 2, origin[1])
                if vertical_centered:
                    origin = self.move_to_coord(origin[0], origin[1] + (size - (size - rate)) // 2)
                size -= rate
            elif growth == LOGARITHMIC:
                if horizontal_centered:
                    origin = self.move_to_coord(origin[0] + (size - (size ** (1 / rate))) // 2, origin[1])
                if vertical_centered:
                    origin = self.move_to_coord(origin[0], origin[1] + (size - (size ** (1 / rate))) // 2)
                size = size ** (1 / rate)
            else:
                print("Growth error: invalid parameter: " + growth)
                return False
        return inspect.stack()[0][3]

    # TESSELLATIONS

    @filename
    def triangle_tessellation(self, length, dimensions):
        """Draws a tiling of regular triangles of a given dimensions."""
        for _ in range(dimensions):
            origin = self.cursor.pos()
            for _ in range(dimensions):
                self.triangle(length)
                self.cursor.forward(length)
            self.move_to_coord(origin[0], origin[1])
            self.move_left(60, length)
        return inspect.stack()[0][3]

    @filename
    def square_tessellation(self, length, dimensions):
        """Draws a tiling of regular squares of a given dimensions."""
        for _ in range(dimensions):
            origin = self.cursor.pos()
            for _ in range(dimensions):
                self.square(length)
                self.cursor.forward(length)
            self.move_to_coord(origin[0], origin[1])
            self.move_left(90, length)
        return inspect.stack()[0][3]

    @filename
    def hexagon_tessellation(self, length, dimensions):
        """Draws a tiling of regular hexagons of a given dimensions."""
        for _ in range(dimensions):
            origin = self.cursor.pos()
            for _ in range(dimensions):
                self.hexagon(length)
                self.move_left(0, length)
                self.move_left(60, length)
            self.move_to_coord(origin[0], origin[1])
            self.move_left(0, length)
            self.move_right(60, length)
        return inspect.stack()[0][3]

    # FRACTALS

    @filename
    def sierpinski_triangle(self, size, depth, color=None):
        """Draws the sierpinski triangle fractal of the given depth and size."""
        if self.valid_color(color):
            self.start_color(color)
        self.sierpinski_triangle_recursive(size, depth, color)
        return inspect.stack()[0][3]

    def sierpinski_triangle_recursive(self, size, depth, color):
        """Helper function to sierpinski_triangle."""
        if depth == 0:
            self.triangle(size, color)
        else:
            self.sierpinski_triangle_recursive(size / 2, depth - 1, color)
            self.cursor.forward(size / 2)
            self.sierpinski_triangle_recursive(size / 2, depth - 1, color)
            self.cursor.backward(size / 2)
            self.cursor.left(60)
            self.cursor.forward(size / 2)
            self.cursor.right(60)
            self.sierpinski_triangle_recursive(size / 2, depth - 1, color)
            self.cursor.left(60)
            self.cursor.backward(size / 2)
            self.cursor.right(60)

    @filename
    def sierpinski_carpet(self, depth, size, x, y, color):
        """Draws the sierpinski carpet fractal of the given depth and size."""
        if self.valid_color(color):
            self.start_color(color)
        self.sierpinski_carpet_recursive(depth, size, x, y, color)
        return inspect.stack()[0][3]

    def sierpinski_carpet_recursive(self, depth, size, x, y, color=None):
        """Recursive helper function to sierpinski_carpet."""
        if depth == 0:
            self.cursor.penup()
            self.cursor.goto(x, y)
            self.cursor.pendown()
            self.square(size, color)
            if self.valid_color(color):
                self.start_color(color)
            self.square(size, color)
            self.cursor.end_fill()

        else:
            new_size = size / 3
            self.sierpinski_carpet_recursive(depth - 1, new_size, x, y, color)
            self.sierpinski_carpet_recursive(depth - 1, new_size, x + new_size, y, color)
            self.sierpinski_carpet_recursive(depth - 1, new_size, x + 2 * new_size, y, color)
            self.sierpinski_carpet_recursive(depth - 1, new_size, x, y - new_size, color)

            self.sierpinski_carpet_recursive(depth - 1, new_size, x + 2 * new_size, y - new_size, color)
            self.sierpinski_carpet_recursive(depth - 1, new_size, x, y - 2 * new_size, color)
            self.sierpinski_carpet_recursive(depth - 1, new_size, x + new_size, y - 2 * new_size, color)
            self.sierpinski_carpet_recursive(depth - 1, new_size, x + 2 * new_size, y - 2 * new_size, color)

    @filename
    def fractal_tree(self, size, depth):
        """Draws a fractal tree of a given depth and starting length."""
        self.fractal_tree_recursive(size, depth)
        return inspect.stack()[0][3]

    def fractal_tree_recursive(self, size, depth):
        """Recursive helper to fractal_tree."""
        if depth == 0:
            return
        self.cursor.forward(size)
        self.cursor.left(30)
        self.fractal_tree(size / 2, depth - 1)
        self.cursor.right(60)
        self.fractal_tree(size / 2, depth - 1)
        self.cursor.left(30)
        self.cursor.backward(size)

    @filename
    def star_of_lakshmi(self, size, color_map=None):
        """Draws the eight-sided star of Lakshmi from Hinduism. Lakshmi is the Hindu goddess of wealth."""
        if not self.valid_color_map(color_map):
            return False
        color_map = self.set_color_map(color_map, 2)

        self.square(size, color_map[0])
        self.move_by_pixels(size / 2, -(size / 4.8))
        self.cursor.left(45)
        self.square(size, color_map[1])

        return f"star-of-lakshmi/star-of-lakshmi-{size}-{color_map[0]}-{color_map[1]}.svg"

    # MOVEMENT

    def move_to_coord(self, x, y) -> tuple:
        """Moves cursor to given coordinates and returns new coordinate as tuple."""
        self.cursor.penup()
        self.cursor.goto(x, y)
        self.cursor.pendown()
        return self.cursor.pos()

    def move_by_pixels(self, x, y):
        """Moves cursor to current coordinates plus given values."""
        origin = self.cursor.pos()
        self.cursor.penup()
        self.cursor.goto(origin[0] + x, origin[1] + y)
        self.cursor.pendown()
        return self.cursor.pos()

    def move_left(self, angle, length):
        """Moves by the given length at the given left angle relative to the current direction."""
        self.cursor.penup()
        self.cursor.left(angle)
        self.cursor.forward(length)
        self.cursor.right(angle)
        self.cursor.pendown()
        return self.cursor.pos()

    def move_right(self, angle, length):
        """Moves by the given length at the given right angle relative to the current direction."""
        self.cursor.penup()
        self.cursor.right(angle)
        self.cursor.forward(length)
        self.cursor.left(angle)
        self.cursor.pendown()
        return self.cursor.pos()

    # COLORING

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

    @staticmethod
    def valid_color(color):
        """Returns True if color is valid, false otherwise."""
        if isinstance(color, str):
            return is_color_like(color)
        elif isinstance(color, tuple):
            return is_color_like(color[0]) and is_color_like(color[1])
        return False

    def start_color(self, color):
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

    # WRAPPERS

    @staticmethod
    def filename(func):
        def render_metadata_string(*args, **kwargs):
            parameters = locals()
            func_name = func(*args, **kwargs)
            formatted_parameters = [arg for arg in parameters['args']][1:]
            metadata = f"{func_name}/{func_name}"
            for para in formatted_parameters:
                if callable(para):
                    continue
                if isinstance(para, list):
                    metadata += "_"
                    metadata += "".join([f"{item}" for item in para])
                else:
                    metadata += f"_{para}"
            return f"{metadata}.svg"
        return render_metadata_string


if __name__ == '__main__':
    geo = Geometry(1, True)
    filename = geo.flower(SQUARE, 100, 4, [("red", "blue"), ("green", "yellow")])
    if geo.export_as_svg:
        if not os.path.exists(f"{filename.split('/')[0]}"):
            os.mkdir(f"{filename.split('/')[0]}")
        geo.cursor.save_as(filename)
    else:
        done()

from svg_turtle import SvgTurtle
from turtle import *
import math as m
import os
from matplotlib.colors import is_color_like
import inspect


SPEED = 'fastest'
THICKNESS = 5
PHI = 1.618033988749
DIAGONAL_CORRECTION = 0.70710678118


class Geometry:

    def __init__(self, line_thickness):
        self.cursor = Turtle()
        self.cursor.speed(SPEED)
        self.cursor.width(line_thickness)
        self.cursor.hideturtle()
        self.export_as_svg = False
        screensize(canvwidth=1080, canvheight=720)

    # BASIC SHAPES

    def circle(self, circumference, color=None):
        """Draws a circle of the given circumference."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        self.cursor.circle(circumference // 2, steps=360)
        self.cursor.end_fill()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def triangle(self, length, color=None):
        """Draws a regular triangle of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(3):
            self.cursor.forward(length)
            self.cursor.left(360 / 3)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def golden_triangle(self, base_length, color=None):
        """Draws a golden triangle of the given base length."""
        parameters = locals()
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
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def square(self, length, color=None):
        """Draws a square of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(360 / 4)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def rectangle(self, length, color=None, export=False):
        """Draws a rectangle of the given side length."""
        parameters = locals()

        self.toggle_cursor(export)
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(90)
            self.cursor.forward(length * 2)
            self.cursor.left(90)
        self.cursor.end_fill()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def rhombus(self, length, angle, color=None):
        """Draws a parallelogram of the given length and height."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(angle)
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
        self.cursor.end_fill()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def parallelogram(self, length, height, angle, color=None):
        """Draws a parallelogram of the given length and height."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
            self.cursor.forward(height)
            self.cursor.left(angle)
        self.cursor.end_fill()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def pentagon(self, length, color=None, export=False):
        """Draws a regular pentagon of the given side length."""
        parameters = locals()
        self.toggle_cursor(export)
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(5):
            self.cursor.forward(length)
            self.cursor.left(360 / 5)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def hexagon(self, length, color=None):
        """Draws a regular hexagon of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(6):
            self.cursor.forward(length)
            self.cursor.left(360 / 6)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def heptagon(self, length, color=None):
        """Draws a regular hexagon of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(7):
            self.cursor.forward(length)
            self.cursor.left(360 / 7)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def octagon(self, length, color=None):
        """Draws a regular octagon of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(8):
            self.cursor.forward(length)
            self.cursor.left(360 / 8)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def nonagon(self, length, color=None):
        """Draws a regular nonagon of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(9):
            self.cursor.forward(length)
            self.cursor.left(360 / 9)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def decagon(self, length, color=None):
        """Draws a regular decagon of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(10):
            self.cursor.forward(length)
            self.cursor.left(360 / 10)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def hendecagon(self, length, color=None):
        """Draws a regular hendecagon of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(11):
            self.cursor.forward(length)
            self.cursor.left(360 / 11)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def dodecagon(self, length, color=None):
        """Draws a regular dodecagon of the given side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(12):
            self.cursor.forward(length)
            self.cursor.left(360 / 12)
        self.cursor.end_fill()
        self.cursor.left(360)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def n_agon(self, sides, length, color=None):
        """Draws a regular polygon of the given number of sides and side length."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        for _ in range(sides):
            self.cursor.forward(length)
            self.cursor.left(360 / sides)
        self.cursor.end_fill()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def irregular_polygon(self, sides, lengths, angles, color=None):
        """Draws an irregular polygon of the given sides, lengths, and angles."""
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)

        for i in range(0, sides):
            self.cursor.forward(lengths[i])
            self.cursor.left(angles[i])
        self.cursor.end_fill()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    # TESSELLATIONS

    def triangle_tessellation(self, length, dimensions):
        parameters = locals()
        for _ in range(dimensions):
            origin = self.cursor.pos()
            for _ in range(dimensions):
                self.triangle(length)
                self.cursor.forward(length)
            self.move_to_coord(origin[0], origin[1])
            self.move_left(60, length)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def square_tessellation(self, length, dimensions):
        parameters = locals()
        for _ in range(dimensions):
            origin = self.cursor.pos()
            for _ in range(dimensions):
                self.square(length)
                self.cursor.forward(length)
            self.move_to_coord(origin[0], origin[1])
            self.move_left(90, length)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:3])

    def hexagon_tessellation(self, length, dimensions):
        parameters = locals()
        for _ in range(dimensions):
            origin = self.cursor.pos()
            for _ in range(dimensions):
                self.hexagon(length)
                self.move_left(0, length)
                self.move_left(60, length)
            self.move_to_coord(origin[0], origin[1])
            self.move_left(0, length)
            self.move_right(60, length)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:3])

    # FRACTALS

    def sierpinski_triangle(self, size, depth, color=None):
        parameters = locals()
        if self.valid_color(color):
            self.start_color(color)
        self.sierpinski_triangle_recursive(size, depth, color)
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

    def sierpinski_triangle_recursive(self, size, depth, color):
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

    def sierpinski_carpet(self, depth, size, x, y, color):
        """Draws a sierpinski carpet fractal of a given depth and size."""
        if self.valid_color(color):
            self.start_color(color)
        self.sierpinski_carpet_recursive(depth, size, x, y, color)
        parameters = locals()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

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

    def fractal_tree(self, size, depth):
        """Draws a fractal tree of a given depth and starting length."""
        self.fractal_tree_recursive(size, depth)
        parameters = locals()
        return self.render_metadata_string(inspect.stack()[0][3], [parameters[arg] for arg in parameters][1:])

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

    # SACRED GEOMETRY

    # def vesica_pisces(self, size):
    #     self.vesica_circle(size, 1)
    #
    # def seed_of_life(self, circumference):
    #     radius = circumference // 2
    #     center = self.cursor.pos()
    #     self.move_to_coord(center[0], center[1] - radius)
    #     self.circle(circumference)
    #     self.move_to_coord(center[0], center[1])
    #     self.flower(self.circle, circumference, 6)
    #
    # @staticmethod
    # def flower_of_life(circumference):
    #     radius = circumference // 2
    #     geo.flower(geo.seed_of_life, circumference, 6, 30, radius)

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
        print('Invalid color parameter')
        return False

    def start_color(self, color):
        """Takes color parameter and sets colors using Turtle functions."""
        if isinstance(color, str):
            self.cursor.pencolor(color)
            self.cursor.begin_fill()
            self.cursor.fillcolor(color)
        elif isinstance(color, tuple):
            if color[0]:
                print(color[0])
                self.cursor.pencolor(color[0])
            if color[1]:
                self.cursor.begin_fill()
                self.cursor.fillcolor(color[1])

    # EXPORT & CURSOR SETTINGS

    def toggle_cursor(self, export):
        """Toggles cursor based on value of boolean variable export."""
        if export:
            self.cursor = SvgTurtle(1000, 1000)
        else:
            self.cursor = Turtle()

        self.cursor.speed(SPEED)
        self.cursor.width(THICKNESS)
        self.cursor.hideturtle()
        return export

    @staticmethod
    def render_metadata_string(func_name, func_parameters):
        """Returns a filepath made up of the function name and parameters"""
        metadata = f"{func_name}/{func_name}"
        for para in func_parameters:
            metadata += f"_{para}"
        return f"{metadata}.svg"


if __name__ == '__main__':
    geo = Geometry()
    export = geo.toggle_cursor(True)
    filename = geo.hexagon(100, ("BLACK", "GREEN"))

    if export:
        if not os.path.exists(f"{filename.split('/')[0]}"):
            os.mkdir(f"{filename.split('/')[0]}")
        geo.cursor.save_as(filename)
    else:
        done()

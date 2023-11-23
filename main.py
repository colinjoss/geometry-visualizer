from svg_turtle import SvgTurtle
from turtle import *
import math as m
import os
from matplotlib.colors import is_color_like
import inspect
import tkinter as _

_.ROUND = _.BUTT

SPEED = "fastest"

PIXELS_PER_INCH = 96
TILE_UNIT_32 = PIXELS_PER_INCH / 32  # 3
TILE_UNIT_16 = PIXELS_PER_INCH / 16  # 6
TILE_UNIT = TILE_UNIT_16
CANVAS_TILE_UNIT_LENGTH = 64
CANVAS_PIXEL_LENGTH = CANVAS_TILE_UNIT_LENGTH * TILE_UNIT  # 384

FULL_CANVAS = CANVAS_PIXEL_LENGTH - TILE_UNIT
TWO_THIRDS_CANVAS = (CANVAS_PIXEL_LENGTH / 3) * 2 - TILE_UNIT
HALF_CANVAS = CANVAS_PIXEL_LENGTH / 2 - TILE_UNIT
THIRD_CANVAS = CANVAS_PIXEL_LENGTH / 3 - TILE_UNIT
QUARTER_CANVAS = CANVAS_PIXEL_LENGTH / 4 - TILE_UNIT
EIGHTH_CANVAS = CANVAS_PIXEL_LENGTH / 8 - TILE_UNIT
NINTH_CANVAS = CANVAS_PIXEL_LENGTH / 9 - TILE_UNIT
SIXTEENTH_CANVAS = CANVAS_PIXEL_LENGTH / 16 - TILE_UNIT

STANDARD_SIZES = [FULL_CANVAS, HALF_CANVAS, TWO_THIRDS_CANVAS, THIRD_CANVAS, QUARTER_CANVAS, EIGHTH_CANVAS, NINTH_CANVAS, SIXTEENTH_CANVAS]
STANDARD_SIZES_NAME_MAP = {
    FULL_CANVAS: "full",
    TWO_THIRDS_CANVAS: "two_third_canvas",
    HALF_CANVAS: "half",
    THIRD_CANVAS: "third",
    QUARTER_CANVAS: "quarter",
    EIGHTH_CANVAS: "eighth",
    NINTH_CANVAS: "ninth",
    SIXTEENTH_CANVAS: "sixteenth"
}

PHI = 1.618033988749
DIAGONAL_CORRECTION = 0.70710678118

AUTO = "auto"

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

CLOVER = "clover"

CONSTANT = "constant"
LOGARITHMIC = "logarithmic"


def color(func):
    def render_color(geometry, *args):
        print("Color args: ", geometry, args)
        if geometry.valid_color(args[-1]):
            print(f"Color: {args[-1]}")
            geometry.start_color(args[-1])
            args = args[:-1]

        if args[-1] == (None, None):
            args = args[:-1]

        metadata = func(geometry, *args)
        geometry.cursor.end_fill()
        return metadata
    return render_color


def filename(func):
    def render_metadata_string(*args):
        print("Metadata string args: ", args)
        print(STANDARD_SIZES)
        parameters = locals()
        func_name = func(*args)
        formatted_parameters = [arg for arg in parameters['args']][1:]
        metadata = f"{func_name}/{func_name}"
        for para in formatted_parameters:
            if callable(para):
                continue
            elif para in STANDARD_SIZES:
                print("SIZE MAP: ", STANDARD_SIZES_NAME_MAP[para])
                metadata += f"_{STANDARD_SIZES_NAME_MAP[para]}"
            elif isinstance(para, list):
                metadata += "_"
                metadata += "".join([f"{item}" for item in para])
            else:
                metadata += f"_{para}"
        print(f"Filename: {metadata}")
        return f"{metadata}.svg"
    return render_metadata_string


class Geometry:

    def __init__(self, pen_size, export):
        self.cursor = Turtle()
        self.export_as_svg = False
        if export:
            self.cursor = SvgTurtle(1500, 1500)
            self.export_as_svg = True
        self.cursor.speed(SPEED)
        self.cursor.width(pen_size)

        self.cursor.hideturtle()

        self.name_to_polygon = {
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
            DODECAGON: self.dodecagon,
        }
        self.name_to_special = {
            CLOVER: self.clover
        }
        self.num_to_polygon_func = {
            1: self.circle,
            3: self.triangle,
            4: self.square,
            5: self.pentagon,
            6: self.hexagon,
            7: self.heptagon,
            8: self.octagon,
            9: self.nonagon,
            10: self.decagon,
            11: self.hendecagon,
            12: self.dodecagon
        }
        self.num_to_polygon = {
            CIRCLE: 1,
            TRIANGLE: 3,
            SQUARE: 4,
            PENTAGON: 5,
            HEXAGON: 6,
            HEPTAGON: 7,
            OCTAGON: 8,
            NONAGON: 9,
            DECAGON: 10,
            HENDECAGON: 11,
            DODECAGON: 12
        }
        self.polygon_to_num = {
            CIRCLE: 1,
            TRIANGLE: 3,
            SQUARE: 4,
            PENTAGON: 5,
            HEXAGON: 6,
            HEPTAGON: 7,
            OCTAGON: 8,
            NONAGON: 9,
            DECAGON: 10,
            HENDECAGON: 11,
            DODECAGON: 12
        }

        screensize(canvwidth=1080, canvheight=720)

    # BASIC SHAPES

    @color
    @filename
    def circle(self, diameter):
        """Draws a circle of the given diameter."""
        self.cursor.circle(diameter / 2, steps=360)
        return inspect.stack()[0][3]

    @filename
    def line(self, length):
        self.cursor.shape("square")
        self.cursor.turtlesize(0.1, 0.1)
        self.cursor.stamp()
        self.cursor.forward(length)
        self.cursor.stamp()
        return inspect.stack()[0][3]

    @color
    @filename
    def triangle(self, length):
        """Draws a regular triangle of the given side length."""
        for _ in range(3):
            self.cursor.forward(length)
            self.cursor.left(360 / 3)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def golden_triangle(self, base_length):
        """Draws a golden triangle of the given base length."""
        origin = self.cursor.pos()
        self.cursor.forward(base_length)
        self.cursor.left(108)
        self.cursor.forward(base_length * PHI)
        self.cursor.left(144)
        self.cursor.forward(base_length * PHI)
        self.cursor.left(108)
        self.move_to_coord(origin[0], origin[1])
        return inspect.stack()[0][3]

    @color
    @filename
    def square(self, length):
        """Draws a square of the given side length."""
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(360 / 4)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def rectangle(self, length, height):
        """Draws a rectangle of the given side length."""
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(90)
            self.cursor.forward(height)
            self.cursor.left(90)
        return inspect.stack()[0][3]

    @color
    @filename
    def rhombus(self, length, angle):
        """Draws a parallelogram of the given length and height."""
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(angle)
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
        return inspect.stack()[0][3]

    @color
    @filename
    def parallelogram(self, length, height, angle):
        """Draws a parallelogram of the given length and height."""
        for _ in range(4):
            self.cursor.forward(length)
            self.cursor.left(180 - angle)
            self.cursor.forward(height)
            self.cursor.left(angle)
        return inspect.stack()[0][3]

    @color
    @filename
    def pentagon(self, length):
        """Draws a regular pentagon of the given side length."""
        for _ in range(5):
            self.cursor.forward(length)
            self.cursor.left(360 / 5)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def hexagon(self, length):
        """Draws a regular hexagon of the given side length."""
        for _ in range(6):
            self.cursor.forward(length)
            self.cursor.left(360 / 6)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def heptagon(self, length):
        """Draws a regular hexagon of the given side length."""
        for _ in range(7):
            self.cursor.forward(length)
            self.cursor.left(360 / 7)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def octagon(self, length):
        """Draws a regular octagon of the given side length."""
        for _ in range(8):
            self.cursor.forward(length)
            self.cursor.left(360 / 8)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def nonagon(self, length):
        """Draws a regular nonagon of the given side length."""
        for _ in range(9):
            self.cursor.forward(length)
            self.cursor.left(360 / 9)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def decagon(self, length):
        """Draws a regular decagon of the given side length."""
        for _ in range(10):
            self.cursor.forward(length)
            self.cursor.left(360 / 10)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def hendecagon(self, length):
        """Draws a regular hendecagon of the given side length."""
        for _ in range(11):
            self.cursor.forward(length)
            self.cursor.left(360 / 11)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def dodecagon(self, length):
        """Draws a regular dodecagon of the given side length."""
        for _ in range(12):
            self.cursor.forward(length)
            self.cursor.left(360 / 12)
        self.cursor.left(360)
        return inspect.stack()[0][3]

    @color
    @filename
    def n_agon(self, length, sides):
        """Draws a regular polygon of the given number of sides and side length."""
        for _ in range(sides):
            self.cursor.forward(length)
            self.cursor.left(360 / sides)
        return inspect.stack()[0][3]

    @color
    @filename
    def irregular_polygon(self, sides, lengths, angles):
        """Draws an irregular polygon of the given sides, lengths, and angles."""
        for i in range(0, sides):
            self.cursor.forward(lengths[i])
            self.cursor.left(angles[i])
        return inspect.stack()[0][3]

    # WONKY SHAPES

    @filename
    def pentasun(self, size, color_map=None):
        """Draws a 'pentasun', a perfect ring of ten pentagons."""
        if not self.valid_color_map(color_map):
            return False
        color_map = self.set_color_map(color_map, 10)
        self.flower(PENTAGON, size, 10, color_map, 0, PHI * size)
        return inspect.stack()[0][3]

    @filename
    def circled_circle(self, diameter, depth):
        radius = diameter // 2
        self.cursor.circle(radius, steps=360)
        angle = 360 // depth
        for _ in range(depth):
            self.cursor.circle(radius, steps=360, extent=angle)
            self.cursor.circle(diameter//depth, steps=360)
        self.cursor.setheading(90)
        self.go((diameter*2)//depth)
        self.cursor.setheading(0)
        self.cursor.circle(radius - ((diameter*2)//depth), extent=360)
        return inspect.stack()[0][3]

    @filename
    def eye_almond(self, diameter, color=None):
        """Generates an eye shape given the circumference of a circle."""
        if color:
            self.start_color(color)
        origin = self.cursor.pos()
        self.cursor.right(55)
        self.cursor.circle(diameter // 2, extent=110, steps=360)
        self.cursor.left(70)
        self.cursor.circle(diameter // 2, extent=110, steps=360)
        self.cursor.right(235)
        self.move_to_coord(origin[0], origin[1])
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def eye_pupil(self, diameter, color_map=None):
        self.shrink(CIRCLE, diameter, 2, CONSTANT, diameter//2, False, True, color_map)
        return inspect.stack()[0][3]

    @filename
    def clover(self, size, depth, color=None):
        """Draws a clover pattern with the given number of petals."""
        if self.valid_color:
            self.start_color(color)
        print(depth)
        angle = 360 // depth
        for _ in range(depth):
            self.cursor.circle(size // 2, steps=360, extent=angle*2)
            self.cursor.left(360-angle)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def bars(self, length, count, spacing):
        if spacing == AUTO:
            empty_space = length - (TILE_UNIT * count)
            spacing = empty_space / (count - 2)
        pos = self.cursor.pos()
        for i in range(0, count):
            self.line(length)
            pos = self.move_to_coord(pos[0], pos[1] + spacing)
        return inspect.stack()[0][3]

    @filename
    def sunshine(self, size, ray_length, rate):
        angle = 360 / rate
        for _ in range(rate):
            self.cursor.right(90)
            self.cursor.forward(ray_length)
            self.cursor.backward(ray_length)
            self.cursor.left(90)
            self.cursor.circle(size * 2, steps=360, extent=angle)
        self.move_right(90, ray_length)
        new_size = (size * 2) + (ray_length * 2) + 100
        self.circle(new_size)
        return inspect.stack()[0][3]

    def fireball(self, size, ray_length, rate):
        angle = 360 // rate
        for _ in range(rate):
            self.move_right(angle, 0)
            self.cursor.forward(ray_length)
            self.cursor.backward(ray_length)
            self.move_left(angle, 0)
            self.cursor.circle(size * 2, steps=360, extent=angle)

    def lumpy_circle(self, size, ray_length, rate):
        angle = 360 // rate
        for _ in range(rate):
            self.move_left(90, 0)
            self.cursor.forward(ray_length)
            self.move_right(90, 0)
            self.cursor.circle(size * 2, steps=360, extent=angle)

    def funky_sun(self, size, rate):
        angle = 360 // rate
        self.cursor.circle(size, steps=360)
        origin = self.cursor.pos()
        heading = 0
        for _ in range(rate):
            self.cursor.right(90)
            self.cursor.circle(25, extent=180)
            self.move_to_coord(origin[0], origin[1])
            self.cursor.circle(size, steps=360, extent=angle)
            origin = self.cursor.pos()
            heading += angle
            self.cursor.setheading(heading)

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

    @filename
    def peppermint(self, size, rate):
        origin = self.cursor.pos()
        angle = 360 // rate
        self.cursor.circle(size, steps=360)
        self.move_to_coord(origin[0], origin[1])
        heading = 0
        for _ in range(rate):
            self.cursor.circle(size//2, extent=180)
            self.move_to_coord(origin[0], origin[1])
            self.cursor.setheading(heading)
            self.cursor.circle(size, steps=360, extent=angle)
            origin = self.cursor.pos()
            heading += angle
        return inspect.stack()[0][3]

    @filename
    def inverse_clover(self, size, depth, color=None):
        if color:
            self.start_color(color)
        angle = 360 / depth
        for _ in range(depth):
            self.cursor.left(angle)
            self.cursor.circle(size // 2, steps=360, extent=angle * 2)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @color
    @filename
    def circle_portion(self, diameter, portion_as_decimal):
        radius = diameter / 2
        angle = 360 * portion_as_decimal
        self.cursor.circle(radius, steps=360, extent=angle)
        origin = self.cursor.pos()
        self.cursor.left(90)
        self.cursor.forward(radius)
        self.cursor.left(180-angle)
        self.cursor.forward(radius)
        self.move_to_coord(origin[0], origin[1])
        self.cursor.left(angle + 90)
        self.cursor.end_fill()
        return inspect.stack()[0][3]

    @filename
    def circle_portion_spiral(self, radius, portions, spiral_depth, color=None):
        if self.valid_color:
            self.start_color(color)
        circle_origin = self.cursor.pos()
        angle = 360 / portions

        self.cursor.circle(radius, steps=360, extent=angle)
        self.move_to_coord(circle_origin[0], circle_origin[1])
        pace = radius / spiral_depth
        meter = pace
        for _ in range(spiral_depth - 1):
            self.cursor.setheading(90)
            self.go(meter)
            self.cursor.setheading(0)
            self.cursor.circle(radius-meter, steps=360, extent=angle)
            meter += pace
            self.move_to_coord(circle_origin[0], circle_origin[1])
        return inspect.stack()[0][3]

    @filename
    def circle_portioned_whole(self, diameter, portion_pattern, color_map=None):
        if not self.valid_portion_pattern(portion_pattern):
            return False
        portion_pattern = self.set_portion_pattern(portion_pattern)
        if not self.valid_color_map(color_map):
            return False
        color_map = self.set_color_map(color_map, len(portion_pattern))

        for i in range(0, len(portion_pattern)):
            self.circle_portion(diameter, portion_pattern[i], color_map[i])
        return inspect.stack()[0][3]

    @filename
    def fibonacci_eye(self, size, triangle_color=None, circle_color_map=None):
        self.triangle(size, triangle_color)
        self.move_by_pixels(size // 2, 0)
        self.shrink(CIRCLE, (size // 2) * (PHI * 0.1 + 1), 2, 'constant', 20, False, True, circle_color_map)
        return inspect.stack()[0][3]

    @filename
    def squiggle(self, size, depth, curve=90):
        for _ in range(depth):
            self.cursor.circle(size//2, extent=curve)
            self.cursor.circle(-(size//2), extent=curve)
            self.cursor.circle(-(size//2), extent=curve)
            self.cursor.circle(size//2, extent=curve)
        return inspect.stack()[0][3]

    @filename
    def zig_zag(self, length, depth, angle):
        for _ in range(depth):
            self.cursor.setheading(0)
            self.cursor.forward(length)
            self.cursor.setheading(angle)
            self.cursor.forward(length)
        return inspect.stack()[0][3]

    @filename
    def square_line(self, length_1, length_2, depth):
        for _ in range(depth):
            self.cursor.setheading(0)
            self.cursor.forward(length_1)
            self.cursor.setheading(90)
            self.cursor.forward(length_2)
            self.cursor.setheading(180)
            self.cursor.forward(length_1)
            self.cursor.setheading(90)
            self.cursor.forward(length_2)
        return inspect.stack()[0][3]

    @filename
    def fibonacci_line(self, length, depth, angle):
        for _ in range(depth):
            self.cursor.setheading(0)
            self.cursor.forward(length)
            length = (length * PHI) - length
            self.cursor.setheading(angle)
            self.cursor.forward(length)
            length = (length * PHI) - length
        return inspect.stack()[0][3]

    @filename
    def amoeba(self, size, depth, large_curve=90, small_curve=90, invert=False):
        invert = -1 if invert else 1
        angle = 360 // depth
        head = 0
        for _ in range(depth):
            self.cursor.setheading(head)
            self.cursor.circle(size//2, extent=large_curve)
            self.cursor.circle(-(size//4), extent=small_curve)
            self.cursor.circle(-(size//4), extent=small_curve)
            self.cursor.circle(size//2, extent=large_curve)
            head += (angle * invert)
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
            self.num_to_polygon_func[y-3](length, color_map[i])
            self.cursor.forward(length)
            self.cursor.right(angle)
        return inspect.stack()[0][3]

    @filename
    def flower(self, polygon, size, depth, angle=0, spacing=0, color_map=None,):
        """Draws the given regular polygon in a seed of life formation."""
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, depth)
        for i in range(0, depth):
            self.move_left(angle, spacing)
            self.name_to_polygon[polygon](size, color_map[i])
            self.cursor.left(360 / depth)
        return inspect.stack()[0][3]

    @filename
    def shrink(self, polygon, size, depth, growth, rate, horizontal_centered=False, vertical_centered=False, color_map=None):
        """Draws given shape in overlapping growth pattern."""
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, depth)
        origin = self.cursor.pos()
        for i in range(0, depth):
            self.name_to_polygon[polygon](size, color_map[i])
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

    @filename
    def star(self, polygon, size, depth, rate):
        """Draws the give polygon with copies of itself radiating out from it."""
        if polygon == CIRCLE:
            return self.star_circle(size, depth, rate)
        origin = self.cursor.pos()
        self.name_to_polygon[polygon](size)
        angle = 360 // self.polygon_to_num[polygon]
        heading = 0
        for _ in range(0, self.polygon_to_num[polygon]):
            self.cursor.setheading(heading)
            for _ in range(0, depth):
                self.go(size * rate)
                self.name_to_polygon[polygon](size)
            self.move_to_coord(origin[0], origin[1])
            origin = self.go(size)
            heading += angle
        return inspect.stack()[0][3]

    def star_circle(self, size, depth, rate):
        """An edge case for the function star that does circles."""
        self.circle(size)
        self.cursor.setheading(90)
        self.go(size//2)
        origin = self.cursor.pos()
        headings = [15, 75, 135, 195, 255, 315]
        for i in range(0, 6):
            self.cursor.setheading(headings[i])
            self.cursor.forward(size)
            for _ in range(0, depth):
                self.go(size * rate)
                self.circle(size)
            self.move_to_coord(origin[0], origin[1])
        return inspect.stack()[0][3]

    @filename
    def column(self, polygon, size, depth, spacing, color_map=None):
        """Generates given shape in vertical chain pattern."""
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, depth)
        for i in range(0, depth):
            position = self.cursor.pos()
            self.name_to_polygon[polygon](size, color_map[i])
            self.move_to_coord(position[0], position[1] + spacing)
        return inspect.stack()[0][3]

    @filename
    def row(self, polygon, size, depth, spacing, color_map=None):
        """Generates given shape in horizontal chain pattern."""
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, depth)
        for i in range(0, depth):
            position = self.cursor.pos()
            self.name_to_polygon[polygon](size, color_map[i])
            self.move_to_coord(position[0] + spacing, position[1])
        return inspect.stack()[0][3]

    @filename
    def ray(self, polygon, size, depth, spacing, color_map=None):
        """Generates given shape in diagonal chain pattern."""
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, depth)
        spacing = float(spacing) * DIAGONAL_CORRECTION
        for i in range(0, depth):
            position = self.cursor.pos()
            self.name_to_polygon[polygon](size, color_map[i])
            self.move_to_coord(position[0] + spacing, position[1] + spacing)
        return inspect.stack()[0][3]

    @filename
    def grid(self, polygon, size, dimensions, spacing=AUTO, color_map=None):
        if self.valid_color_map(color_map):
            color_map = self.set_color_map(color_map, dimensions[1])
        if not isinstance(dimensions, tuple):
            print("Invalid dimensions: Must be expressed as tuple")
            return False
        if not isinstance(dimensions[0], int) or not isinstance(dimensions[1], int):
            print("Invalid dimensions: Tuple items must be integers")
            return False
        if spacing == AUTO:
            spacing = size

        for _ in range(dimensions[0]):
            pos = self.cursor.pos()
            self.row(polygon, size, dimensions[1], spacing, color_map)
            self.move_to_coord(pos[0], pos[1] - spacing)
        return inspect.stack()[0][3]

    # SACRED GEOMETRY & NAMED SYMBOLS

    @filename
    def yin_yang(self):
        """Draws the yin-yang."""
        self.cursor.circle(100, 180)
        self.cursor.circle(50, 180)
        self.cursor.circle(-50, 180)
        self.cursor.circle(-100, 180)
        return inspect.stack()[0][3]

    @filename
    def vesica_pisces(self, size):
        """Draws the Vesica Pisces."""
        self.vesica_circle(size, 1)
        return inspect.stack()[0][3]

    @filename
    def seed_of_life(self, diameter):
        """Draws the Seed of Life"""
        radius = diameter // 2
        center = self.cursor.pos()
        self.move_to_coord(center[0], center[1] - radius)
        self.circle(diameter)
        self.move_to_coord(center[0], center[1])
        self.flower(CIRCLE, diameter, 6)
        return inspect.stack()[0][3]

    @filename
    def quincunx(self, diameter, polygon):
        node_diameter = diameter / 3
        pos = self.cursor.pos()
        # Bottom row
        self.name_to_polygon[polygon](node_diameter)
        self.move_by_pixels(node_diameter * 2, 0)
        self.name_to_polygon[polygon](node_diameter)
        # Middle
        self.move_to_coord(pos[0], pos[1])
        self.move_by_pixels(node_diameter, node_diameter)
        self.name_to_polygon[polygon](node_diameter)
        # Top row
        self.move_to_coord(pos[0], pos[1])
        self.move_by_pixels(0, node_diameter * 2)
        self.name_to_polygon[polygon](node_diameter)
        self.move_by_pixels(node_diameter * 2, 0)
        self.name_to_polygon[polygon](node_diameter)

        return inspect.stack()[0][3]

    @filename
    def vesica(self, polygon, width, depth=1):
        if polygon == CIRCLE:
            self.vesica_circle(width, depth)
        elif polygon == TRIANGLE:
            self.vesica_triangle(width, depth)
        elif polygon == SQUARE:
            self.vesica_square(width, depth)
        elif polygon == PENTAGON:
            self.vesica_pentagon(width, depth)
        elif polygon == HEXAGON:
            self.vesica_hexagon(width, depth)
        else:
            print("That shape cannot be used.")
            return None
        return inspect.stack()[0][3]

    def vesica_circle(self, width, depth):
        i = 0
        origin = self.cursor.pos()
        while i < depth:
            self.circle(width)
            self.circle(width // 1.5)
            self.move_to_coord(origin[0], origin[1] + width // 3)
            origin = self.cursor.pos()
            self.circle(width // 1.5)
            self.circle(width // 3)
            width = width // 3
            i += 1

    def vesica_triangle(self, width, depth):
        i = 0
        origin = self.cursor.pos()
        while i < depth:
            self.triangle(width)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.triangle(width // 1.5)
            origin = self.move_to_coord(origin[0], origin[1] + width // 3.444)
            self.triangle(width // 1.5)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.triangle(width // 3)
            width = width // 3
            i += 1

    def vesica_square(self, width, depth):
        i = 0
        origin = self.cursor.pos()
        while i < depth:
            self.square(width)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.square(width // 1.5)
            origin = self.move_to_coord(origin[0], origin[1] + width // 3)
            self.square(width // 1.5)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.square(width // 3)
            width = width // 3
            i += 1

    def vesica_pentagon(self, width, depth):
        i = 0
        origin = self.cursor.pos()
        while i < depth:
            self.pentagon(width)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.pentagon(width // 1.5)
            origin = self.move_to_coord(origin[0], origin[1] + width // 1.948)
            self.pentagon(width // 1.5)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.pentagon(width // 3)
            width = width // 3
            i += 1

    def vesica_hexagon(self, width, depth):
        i = 0
        origin = self.cursor.pos()
        while i < depth:
            self.hexagon(width)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.hexagon(width // 1.5)
            origin = self.move_to_coord(origin[0], origin[1] + width // 1.723)
            self.hexagon(width // 1.5)
            origin = self.move_to_coord(origin[0] + width // 6, origin[1])
            self.hexagon(width // 3)
            width = width // 3
            i += 1

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
    def sierpinski_triangle(self, size, depth, segment=2, color=None):
        """Draws the sierpinski triangle fractal of the given size, depth, and number of segments squared."""
        if self.valid_color(color):
            self.start_color(color)
        if segment < 2:
            print("Segment error: Must be int greater than 1")
            return False
        self.sierpinski_triangle_recursive(size, depth, segment, color)
        return inspect.stack()[0][3]

    def sierpinski_triangle_recursive(self, size, depth, seg, color):
        """Helper function to sierpinski_triangle."""
        if depth == 0:
            self.triangle(size, color)
        else:
            layer = seg
            for _ in range(seg):
                for _ in range(layer):
                    self.sierpinski_triangle_recursive(size / seg, depth - 1, seg, color)
                    self.cursor.forward(size / seg)
                for _ in range(layer):
                    self.cursor.backward(size / seg)
                self.cursor.left(60)
                self.cursor.forward(size / seg)
                self.cursor.right(60)
                layer -= 1
            self.cursor.left(60)
            for _ in range(seg):
                self.cursor.backward(size / seg)
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

    def go(self, length):
        """Go forward by a given length without marking the canvas."""
        self.cursor.penup()
        self.cursor.forward(length)
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

    @staticmethod
    def valid_portion_pattern(portion_pattern):
        if isinstance(portion_pattern, int):
            return True
        if isinstance(portion_pattern, list):
            if not all(isinstance(portion, float) for portion in portion_pattern):
                print('Invalid portion_pattern parameter: list must contain only float elements')
                return False
            if round(sum(portion_pattern), 1) != 1.0:
                print('Invalid portion_pattern parameter: portions must sum to 1.0')
                return False
            return True
        print('Invalid portion_pattern parameter: must be list or int')
        return False

    @staticmethod
    def set_portion_pattern(portion_pattern):
        if isinstance(portion_pattern, int):
            return [(100 / portion_pattern) / 100 for _ in range(0, portion_pattern)]
        return portion_pattern


if __name__ == '__main__':
    geo = Geometry(TILE_UNIT, True)
    filename = geo.square(HALF_CANVAS)
    if geo.export_as_svg:
        if not os.path.exists(f"{filename.split('/')[0]}"):
            os.mkdir(f"{filename.split('/')[0]}")
        geo.cursor.save_as(filename)
    else:
        done()

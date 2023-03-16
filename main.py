from svg_turtle import SvgTurtle
from turtle import *
from CONSTANTS import *


class Geometry:
    def __init__(self):
        self.cursor = Turtle()
        if SVG:
            self.cursor = SvgTurtle(2500, 2500)
        self.cursor.speed(SPEED)
        self.cursor.width(THICKNESS)
        self.cursor.hideturtle()
        screensize(canvwidth=1080, canvheight=720)


if __name__ == '__main__':
    geo = Geometry()

    if SVG:
        geo.cursor.save_as('test.svg')
    else:
        done()

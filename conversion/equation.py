from math import sqrt, sin, pi


def compute_pentagon_side_from_diagonal(diagonal):
    return diagonal / ((1 + sqrt(5)) / 2)


def compute_pentagon_inscribed_side(diameter):
    return compute_inscribed_side(5, diameter / 2)


def compute_inscribed_side(sides, radius):
    theta = 360 / sides
    theta_in_radians = theta * 3.14 / 180
    return 2 * radius * sin(theta_in_radians / 2)
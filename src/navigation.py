import math

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def heading(x, y, tx, ty):
    return math.atan2(ty - y, tx - x)
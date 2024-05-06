from point import Point
from shapes.simple_shape import SimpleShape
# import for drawing
import matplotlib.pyplot as plt
import numpy as np
from colors import *
import cv2 as cv

class Line(SimpleShape):
    def __init__(self, point1: Point, point2: Point,  color:RGB = BLACK):
        super().__init__([point1,point2],color, None)


from shapes.point import Point
from shapes.simple_shape import SimpleShape
import numpy as np
import cv2 as cv
from colors import *

class Triangle(SimpleShape):
    def __init__(self, point1: Point, point2: Point, point3: Point, color:RGB = BLACK, fill_color:RGB = WHITE):
        self.color = color
        self.__assert_points_are_triangle(point1, point2, point3)
        super().__init__([point1,point2,point3],color, fill_color)
        # self.lines = [Line(self.point1, self.point2, color),
        #               Line(self.point2, self.point3, color),
        #               Line(self.point3, self.point1, color)]

    def __assert_points_are_triangle(self, point1, point2, point3):
        if point1 == point2 or point1 == point3 or point2 == point3:
            raise ValueError("All points should be different")
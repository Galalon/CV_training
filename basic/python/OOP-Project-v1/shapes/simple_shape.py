
from matplotlib import pyplot as plt
from shapes.point import Point
import cv2 as cv
from colors import *
import numpy as np
from shapes.shape import Shape

class SimpleShape(Shape):

    def __init__(self,points: list[Point], color:RGB = BLACK ,fill_color:RGB = WHITE):
        self.color = color
        self.fill_color = fill_color
        self.points: np.ndarray[Point] = np.array(points)

    # THIS VIOLATES THE LSP (Liskov Substitution Principle) because classes use this without overriding it
    def draw(self, img:plt.figure):
        points_for_draw = np.array([[pt.get_tuple() for pt in self.points]])
        if self.fill_color:
            cv.fillPoly(img, points_for_draw, self.fill_color)
        cv.polylines(img, points_for_draw, True, self.color, BORDER_THICKNESS)
    
    def rotate_by_center(self, center_point:Point, angle: float):
        for point in self.points:
            point.rotate(center_point, angle)

    def rotate(self, angle: float):
        center_point = self.get_center_point()
        self.rotate_by_center(center_point, angle)

    def translate(self, x: int, y: int):
        for point in self.points:
            point.translate(x, y)

    def get_center_point(self):
        xs = [point.x for point in self.points]
        ys = [point.y for point in self.points]
        return Point(sum(xs)/len(self.points), sum(ys)/len(self.points))

    def scale(self, factor: float):
        center_point = self.get_center_point()
        for point in self.points:
            point.scale(center_point, factor)

    def get_points(self,):
        return self.points
        


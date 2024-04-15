from shapes.point import Point
from shapes.simple_shape import SimpleShape
import cv2 as cv
import numpy as np
from colors import *

class Circle(SimpleShape):
    def __init__(self, center_point:Point, radius: int,  color:RGB = BLACK, fill_color:RGB = WHITE):
        super().__init__([center_point],color, fill_color)
        self.radius = int(radius)

    def draw(self, img:np.ndarray):
        center_point = self.points[0].get_tuple()
        if self.fill_color:
            cv.circle(img, center_point, self.radius, self.fill_color, cv.FILLED)
        cv.circle(img, center_point, self.radius, self.color, BORDER_THICKNESS)

    def scale(self, factor: float):
        self.radius *= factor

    
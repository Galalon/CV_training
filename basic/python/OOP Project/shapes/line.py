from point import Point
from shape import Shape
# import for drawing
import matplotlib.pyplot as plt
import numpy as np
from colors import *
import cv2 as cv

class Line(Shape):
    def __init__(self, point1: Point, point2: Point,  color:RGB = BLACK):
        self.point1 = point1
        self.point2 = point2
        self.color = color
        super().__init__([point1,point2],color, None)


    def draw(self, img:np.ndarray):
        cv.line(img, self.point1.get_tuple(), self.point2.get_tuple(), self.color, BORDER_THICKNESS)
        


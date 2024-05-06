from shapes.point import Point
from shapes.shape import Shape
import cv2 as cv
import numpy as np
from colors import *

class Rectangle(Shape):
    def __init__(self, center_point:Point, width: float, height: float, color:RGB = BLACK, fill_color:RGB = WHITE):
        self._center_point = center_point
        self.width = width
        self.height = height
        points = self.__init_points()
        super().__init__(points, color, fill_color)

    def __init_points(self):
        new_points = [self.__get_low_left_point(), self.__get_low_right_point(), self.__get_top_right_point(), self.__get_top_left_point()]
        return new_points
            
    def __get_low_left_point(self):
        return Point(self._center_point[0] - self.width/2, self._center_point[1] + self.height/2)
    def __get_low_right_point(self):
        return Point(self._center_point[0] + self.width/2, self._center_point[1] + self.height/2)
    def __get_top_left_point(self):
        return Point(self._center_point[0] - self.width/2, self._center_point[1] - self.height/2)
    def __get_top_right_point(self):
        return Point(self._center_point[0] + self.width/2, self._center_point[1] - self.height/2)
    

    def rotate(self, angle: float):
        center_point = self.get_center_point()
        super().rotate_by_center(center_point, angle)        

    # def draw(self,img:np.ndarray):
        # if self.fill_color:
            # cv.rectangle(img, low_left, up_right, self.fill_color, cv.FILLED)
        # cv.rectangle(img, low_left, up_right, self.color, BORDER_THICKNESS)

       

        
        


class RectangleFactory:
    @staticmethod
    def create_rectangle_from_center_point(center_point:Point, width: float, height: float,  color:RGB = BLACK, fill_color:RGB = WHITE):
        return Rectangle(center_point, width, height, color, fill_color)
    
    @staticmethod
    def create_rectangle_from_low_left_point(low_left_point:Point, width: float, height: float,  color:RGB = BLACK, fill_color:RGB = WHITE):
        return Rectangle(Point(low_left_point.x + width/2, low_left_point.y - height/2), width, height, color, fill_color)
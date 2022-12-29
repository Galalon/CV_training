# from Shapes.BasicShape import BasicShape
import cv2

from OOP.OOP_EX.OOP_EX.Shapes.BasicShape import BasicShape


class Circle(BasicShape):

    def __init__(self, points, radius, color, is_filled):
        super().__init__(points, color)
        self._radius = radius
        self._is_filled = is_filled

    def draw(self, image_to_draw_on):
        thickness = cv2.FILLED if self._is_filled else None
        return cv2.circle(image_to_draw_on, self._points[0], self._radius, self._color, thickness=thickness)

import cv2

from OOP.OOP_EX.OOP_EX.Shapes.BasicShape import BasicShape


class Point(BasicShape):

    def __init__(self, points, color):
        super().__init__(points, color)

    def draw(self, image_to_draw_on):
        return cv2.circle(image_to_draw_on, self._points[0], 1, self._color, thickness=cv2.FILLED)

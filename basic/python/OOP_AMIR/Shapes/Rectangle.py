import cv2
import numpy as np

from OOP.OOP_EX.OOP_EX.Shapes.BasicShape import BasicShape


class Rectangle(BasicShape):

    def __init__(self, points, color, is_filled):
        super().__init__(points, color)
        self._points.append((points[1]["x"], points[0]["y"]))
        self._points.append((points[1]["x"], points[1]["y"]))
        self._points.append((points[0]["x"], points[1]["y"]))
        self._is_filled = is_filled

    def draw(self, image_to_draw_on):
        rect_cnt = np.array([self._points[0], self._points[1], self._points[2], self._points[3]])
        thickness = cv2.FILLED if self._is_filled else None
        return cv2.drawContours(image_to_draw_on, [rect_cnt], 0, self._color, thickness=thickness)

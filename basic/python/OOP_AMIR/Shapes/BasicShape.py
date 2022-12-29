# from Shapes.Shape import Shape
# from Helpers.Geometrics import Geometrics
import abc

from OOP.OOP_EX.OOP_EX.Helpers.Geometrics import Geometrics
from OOP.OOP_EX.OOP_EX.Shapes.Shape import Shape


class BasicShape(Shape, metaclass=abc.ABCMeta):

    def __init__(self, points, color):
        self._points = list()
        self._points.append((points[0]["x"], points[0]["y"]))
        self._color = (color["R"], color["G"], color["B"])

    @abc.abstractmethod
    def draw(self, image_to_draw_on):
        pass

    def rotate(self, angle, center=(0, 0)):
        for i, point in enumerate(self._points):
            new_point = Geometrics.rotate(center, point, angle)
            self._points[i] = (int(round(new_point[0])),
                               int(round(new_point[1])))

    def translate(self, horizontal, vertical):
        for i, point in enumerate(self._points):
            self._points[i] = Geometrics.translate(point, horizontal, vertical)

    def resize(self, factor, center=(0, 0)):
        for i, point in enumerate(self._points):
            new_point = Geometrics.resize(center, point, factor)
            self._points[i] = (int(round(new_point[0])),
                               int(round(new_point[1])))

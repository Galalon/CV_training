import numpy  as np
from shapes.shape import Shape
from shapes.point import Point


class ComplexShape:
    def __init__(self, shapes: list=[]):
        self._shapes = shapes
        
    def draw(self, img:np.ndarray):
        for shape in self._shapes:
            shape.draw(img)

    def translate(self, x: int, y: int):
        for shape in self._shapes:
            shape.translate(x, y)
    
    def rotate_by_center(self, center_point:Point, angle: float):
        for shape in self._shapes:
            shape.rotate_by_center(center_point, angle)

    def rotate(self, angle: float):
        for shape in self._shapes:
            shape.rotate(angle)

    def _add_shape(self, shape):
        self._shapes.append(shape)

    def scale(self, factor: float):
        raise NotImplementedError("Subclass must implement abstract method")

        
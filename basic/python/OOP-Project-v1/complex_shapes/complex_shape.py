import numpy  as np
from shapes.shape import Shape
from shapes.point import Point


class ComplexShape(Shape):
    def __init__(self, shapes: list[Shape]=[]):
        self._shapes:np.ndarray = np.array(shapes)

    def add_shape(self, shape: Shape):
        self._add_shape(shape)
        
    def draw(self, img:np.ndarray):
        for shape in self._shapes:
            shape.draw(img)

    def translate(self, x: int, y: int):
        for shape in self._shapes:
            shape.translate(x, y)
    
    def rotate_by_center(self, center_point:Point, angle: float):
        for shape in self._shapes:
            shape.rotate_by_center(center_point, angle)

    def _add_shape(self, shape):
        self._shapes = self._shapes.append(shape)

    def scale(self, factor: float):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def rotate(self, angle: float):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def get_center_point(self):
        bbox = self._get_bounding_box()

    def _get_all_points(self):

        
    def _get_bounding_box(self):
        # return 4 points that are the corners of the bounding box
        all_points = 
        highest_x, lowest_x = min([])
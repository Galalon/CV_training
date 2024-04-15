import numpy  as np
from shapes.shape import Shape
from shapes.point import Point


class ComplexShape(Shape):
    def __init__(self, shapes: list[Shape]=[]):
        self._shapes: np.ndarray[Shape] = np.array(shapes)

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

    def _add_shape(self, shape: Shape):
        self._shapes = np.append(self._shapes, shape)

    def scale(self, factor: float):
        centers = [shape.get_center_point() for shape in self._shapes]
        complex_center = self.get_center_point()
        for shape, center in zip(self._shapes, centers):
            distance_vector = center - complex_center
            additional_distance = distance_vector * (factor - 1)
            shape.translate(additional_distance[0], additional_distance[1])
            shape.scale(factor)
    
    def rotate(self, angle: float):
        self.rotate_by_center(self.get_center_point(), angle)
    
    def get_center_point(self):
        bbox = self._get_bounding_box()
        xs = [point[0] for point in bbox]
        ys = [point[1] for point in bbox]
        return Point(sum(xs)/len(bbox), sum(ys)/len(bbox))

    def _get_all_points(self):
        arrays = [shape.get_points() for shape in self._shapes]
        return np.concatenate(arrays)
        
    def _get_bounding_box(self):
        # return 4 points that are the corners of the bounding box
        all_points = self._get_all_points()
        xs = [point[0] for point in all_points]
        ys = [point[1] for point in all_points]
        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)
        return [Point(min_x, min_y), Point(max_x, min_y), Point(max_x, max_y), Point(min_x, max_y)]
    
    def get_points(self,):
        return self._get_all_points()
from shape_parser import ShapeParser
from shapes.triangle import Triangle

class TriangleParser(ShapeParser):
    def __init__(self):
        self.arguemnts = ["point1", "point2", "point3"]
        self.optional_arguments = ["color", "fill_color"]

    def parse(self, arguments_dict):
        if not all(arg in arguments_dict for arg in self.arguemnts):
            raise ValueError("Triangle arguments are missing")
        
        point1 = self._parse_point(arguments_dict["point1"])
        point2 = self._parse_point(arguments_dict["point2"])
        point3 = self._parse_point(arguments_dict["point3"])
        color, fill_color = self._parse_colors(arguments_dict)
        
        triangle = Triangle(point1, point2, point3, color, fill_color)
        return triangle
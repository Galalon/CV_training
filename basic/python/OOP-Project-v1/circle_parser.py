from shape_parser import ShapeParser
from shapes.circle import Circle


class CircleParser(ShapeParser):
    def __init__(self):
        self.arguemnts = ["center", "radius"]
        self.optional_arguments = ["color", "fill_color"]

    def parse(self, arguments_dict):
        if not all(arg in arguments_dict for arg in self.arguemnts):
            raise ValueError("Circle arguments are missing")
        
        center = self._parse_point(arguments_dict["center"])
        radius = arguments_dict["radius"]
        color, fill_color = self._parse_colors(arguments_dict)
                
        circle = Circle(center, radius, color, fill_color)
        return circle
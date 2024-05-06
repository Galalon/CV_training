from shape_parser import ShapeParser
from shapes.rectangle import Rectangle, RectangleFactory

class RectangleParser(ShapeParser):
    def __init__(self):
        self.arguemnts = ["center", "width", "height"]
        self.optional_arguments = ["color", "fill_color"]

    def parse(self, arguments_dict):
        if not all(arg in arguments_dict for arg in self.arguemnts):
            raise ValueError("Rectangle arguments are missing")
        
        center = self._parse_point(arguments_dict["center"])
        width = arguments_dict["width"]
        height = arguments_dict["height"]
        color, fill_color = self._parse_colors(arguments_dict)        
        rectangle = RectangleFactory.create_rectangle_from_center_point(center, width, height, color, fill_color)
        return rectangle
    
    
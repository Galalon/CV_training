
from shapes.shape import Shape
from shapes.point import Point
from colors import color_mapping

class ShapeParser:

    def parse(self, arguments_dict) -> Shape:
        raise NotImplementedError("Subclasses must implement abstract method")
    
    def parse_actions(self, shape, actions):
        for action_name in actions:
            if action_name not in ["translate", "rotate", "scale"]:
                raise ValueError("Unknown action")
        
        for action_name, action in actions.items():
            if action_name == "translate":
                self._parse_tranlsate(shape, action)
            elif action_name == "rotate":
                self._parse_rotate(shape, action)
            elif action_name == "scale":
                self._parse_scale(shape, action)
            
    def _parse_tranlsate(self, shape, action):
        if "x" not in action or "y" not in action:
            raise ValueError("Translate action is missing x or y")
        shape.translate(action["x"], action["y"])

    def _parse_rotate(self, shape, action):
        if "angle" not in action:
            raise ValueError("Rotate action is missing angle")
        shape.rotate(action["angle"])

    def _parse_scale(self, shape, action):
        if "factor" not in action:
            raise ValueError("Scale action is missing factor")
        shape.scale(action["factor"])
                

    def _parse_point(self, point_dict):
        if "x" not in point_dict or "y" not in point_dict:
            raise ValueError("Point is missing x or y")
        return Point(point_dict["x"], point_dict["y"])
    
    def _parse_colors(self, shape_dict):
        color = shape_dict.get("color")
        fill_color = shape_dict.get("fill color")

        
        if color:
            color = color_mapping[color]
        if fill_color:
            fill_color = color_mapping[fill_color]
            
        return color, fill_color


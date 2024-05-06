import json
from triangle_parser import TriangleParser
from circle_parser import CircleParser
from rectangle_parser import RectangleParser
from composite_shape_parser import CompositeShapeParser
from shapes.shape import Shape
import numpy as np
import cv2 as cv


class ImageParser:
    def __init__(self):
        self.arguemnts = []
        self.optional_arguments = []

    def _parse_simple_shape(self, shape_dict) -> Shape:
        if "type" not in shape_dict:
            raise ValueError("Shape type is missing")
        match shape_dict["type"]:
            case "triangle":
                shape_parser = TriangleParser()
            case "circle":
                shape_parser = CircleParser()
            case "rectangle":
                shape_parser = RectangleParser()
            case _:
                raise ValueError("Unknown shape type")
            
        shape = shape_parser.parse(shape_dict)
        if "actions" in shape_dict:
            actions = shape_dict["actions"]
            shape_parser.parse_actions(shape, actions)

        return shape

    def _parse_simple_shapes(self, simple_shapes):
        shapes = {}
        for name, shape_dict in simple_shapes.items():
            shape = self._parse_simple_shape(shape_dict)
            shapes[name] = shape
        return shapes
    
    def _parse_composite_shapes(self, composite_shapes, simple_shapes):
        complex_shapes = {}
        for name, shape_dict in composite_shapes.items():
            composite_shape_parser = CompositeShapeParser(simple_shapes | complex_shapes)
            if "shapes" not in shape_dict:
                raise ValueError("Composite shape is missing shapes")
            
            composite_shape = composite_shape_parser.parse(shape_dict)
            complex_shapes[name] = composite_shape
            if "actions" in shape_dict:
                actions = shape_dict["actions"]
                composite_shape_parser.parse_actions(composite_shape, actions)
        return complex_shapes
    
    def parse(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            if "simple shapes" in data:
                simple_shapes = self._parse_simple_shapes(data["simple shapes"])
            if "composite shapes" in data:
                composite_shapes = self._parse_composite_shapes(data["composite shapes"], simple_shapes)
            all_shapes = simple_shapes | composite_shapes
            img = np.zeros((1000,1000,3), np.uint8)
            
            if "draw" in data:
                shapes_to_draw = data["draw"]
                if shapes_to_draw:
                    for shape_name in shapes_to_draw:
                        if not shape_name in all_shapes:
                            raise ValueError(f"Shape {shape_name} is not defined")
                        all_shapes[shape_name].draw(img)
                

            cv.imshow("image", img)
            cv.waitKey(0)
            cv.destroyAllWindows()



    


if __name__ == "__main__":
    parser = ImageParser()
    parser.parse("shapes_file.json")
        
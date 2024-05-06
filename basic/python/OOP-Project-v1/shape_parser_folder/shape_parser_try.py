import json
from shapes.shape import Shape

class ShapeParserTry:

    def __init__(self,):
        self.shapes = []

    def _parse_simple_shape(self, shape)-> Shape:
        if "type" not in shape:
            raise ValueError("Shape type is missing")

    def _parse_simple_shapes(self, shapes):
        
        simple_shapes = {
            shape_name: self._parse_simple_shape(shape) for shape_name, shape in shapes.items()
        }

        return simple_shapes

    def parse(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            if "simple shapes" in data:
                simple_shapes = self._parse_simple_shapes(data["simple shapes"])


# import sys
# sys.path.append('../')   
shape_parser = ShapeParserTry()
shape_parser.parse('shapes_file.json')
    


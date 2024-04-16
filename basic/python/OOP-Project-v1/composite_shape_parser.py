
from shape_parser import ShapeParser
from complex_shapes.complex_shape import ComplexShape
from shapes.shape import Shape
from complex_shapes.house import House
from complex_shapes.city import City
from complex_shapes.neighborhood import Neighborhood

class CompositeShapeParser(ShapeParser):
    # saved_shapes = {"house": House, "city": City, "neighborhood": Neighborhood}
    def __init__(self, existing_shapes: dict[str, Shape]):
        self.existing_shapes = existing_shapes

        
    def parse(self, composite_shape_dict) -> ComplexShape:
        shapes = []
        if "shapes" not in composite_shape_dict:
            raise ValueError("Composite shape is missing shapes")
        for shape in composite_shape_dict["shapes"]:
            if shape not in self.existing_shapes:
                raise ValueError(f"Shape {shape} is not defined")
            concrete_shape = self.existing_shapes[shape].get_copy()
            shapes.append(concrete_shape)

        return ComplexShape(shapes)
        
    

from OOP.OOP_EX.OOP_EX.Shapes.Shape import Shape


class CompositeShape(Shape):

    def __init__(self):
        self._child_shapes = list()

    def draw(self, image_to_draw_on):
        for child in self._child_shapes:
            image_to_draw_on = child.draw(image_to_draw_on)
        return image_to_draw_on

    def rotate(self, angle, center=(0, 0)):
        for child in self._child_shapes:
            child.rotate(angle, center)

    def translate(self, horizontal, vertical):
        for child in self._child_shapes:
            child.translate(horizontal, vertical)

    def resize(self, factor, center=(0, 0)):
        for child in self._child_shapes:
            child.resize(factor, center)

    def add_shape(self, shape: Shape) -> None:
        """

        :param shape: shape to add as part of the CompositeShape
        :return: No return object - adds the shape to _childShapes
        """
        self._child_shapes.append(shape)

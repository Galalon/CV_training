import unittest
from unittest.mock import MagicMock

from OOP.OOP_EX.OOP_EX.Shapes.CompositeShape import CompositeShape


class MyTestCase(unittest.TestCase):
    def test_empty_composite(self):
        shape = CompositeShape()
        self.assertEqual([], shape._child_shapes)

    def test_composite_with_1_basic_shape(self):
        mock_rectangle = MagicMock()
        mock_rectangle._points = [(5, 5), (-5, 5), (-5, -5), (5, -5)]
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle)
        self.assertEqual((5, 5), comp_shape._child_shapes[0]._points[0])
        self.assertEqual((-5, 5), comp_shape._child_shapes[0]._points[1])
        self.assertEqual((-5, -5), comp_shape._child_shapes[0]._points[2])
        self.assertEqual((5, -5), comp_shape._child_shapes[0]._points[3])

    def test_composite_1_basic_shape_rotate(self):
        mock_rectangle = MagicMock()
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle)
        comp_shape.rotate(315)
        mock_rectangle.rotate.assert_called_with(315, (0, 0))

    def test_composite_2_basic_shape_rotate(self):
        mock_rectangle1 = MagicMock()
        mock_rectangle2 = MagicMock()
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle1)
        comp_shape.add_shape(mock_rectangle2)
        comp_shape.rotate(315)
        mock_rectangle1.rotate.assert_called_with(315, (0, 0))
        mock_rectangle2.rotate.assert_called_with(315, (0, 0))

    def test_composite_1_basic_shape_resize(self):
        mock_rectangle = MagicMock()
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle)
        comp_shape.resize(2)
        mock_rectangle.resize.assert_called_with(2, (0, 0))

    def test_composite_nested_rotate(self):
        mock_rectangle1 = MagicMock()
        mock_rectangle2 = MagicMock()
        comp_shape1 = CompositeShape()
        comp_shape1.add_shape(mock_rectangle1)
        comp_shape1.add_shape(mock_rectangle2)

        mock_rectangle3 = MagicMock()
        mock_rectangle4 = MagicMock()
        comp_shape2 = CompositeShape()
        comp_shape2.add_shape(mock_rectangle3)
        comp_shape2.add_shape(mock_rectangle4)

        comp_shape = CompositeShape()
        comp_shape.add_shape(comp_shape1)
        comp_shape.add_shape(comp_shape2)

        comp_shape.rotate(315)
        mock_rectangle1.rotate.assert_called_with(315, (0, 0))
        mock_rectangle2.rotate.assert_called_with(315, (0, 0))
        mock_rectangle3.rotate.assert_called_with(315, (0, 0))
        mock_rectangle4.rotate.assert_called_with(315, (0, 0))


if __name__ == '__main__':
    unittest.main()

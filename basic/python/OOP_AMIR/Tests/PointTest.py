import unittest

import numpy as np

from OOP.OOP_EX.OOP_EX.Shapes.Point import Point


class PointTest(unittest.TestCase):
    def test_point_construct(self):
        point = Point([{"x": 5, "y": 5}], {"R": 255, "G": 0, "B": 0})
        self.assertEqual((5, 5), point._points[0])
        self.assertEqual(1, len(point._points))
        self.assertEqual((255, 0, 0), point._color)

    def test_draw_point_in_image_center(self):
        image_to_draw_on = np.ones((11, 11, 3), np.uint8) * 255
        point_to_draw = Point([{"x": 5, "y": 5}], {"R": 255, "G": 0, "B": 0})
        expected_image = np.ones((11, 11, 3), np.uint8) * 255
        expected_image[5, 5, 1:3] = 0
        expected_image[4, 5, 1:3] = 0
        expected_image[5, 4, 1:3] = 0
        expected_image[6, 5, 1:3] = 0
        expected_image[5, 6, 1:3] = 0
        self.assertTrue(np.array_equal(expected_image, point_to_draw.draw(image_to_draw_on)))


if __name__ == '__main__':
    unittest.main()

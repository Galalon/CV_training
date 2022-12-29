import math
import unittest

from OOP.OOP_EX.OOP_EX.Helpers.Geometrics import Geometrics


class GeometricsTest(unittest.TestCase):
    def test_rotate1(self):
        center = (0, 0)
        point_to_rotate = (-3, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, math.pi / 4)
        self.assertAlmostEqual(-4.2426, new_point[0], places=4)
        self.assertAlmostEqual(0, new_point[1], places=4)

    def test_rotate2(self):
        center = (0, 0)
        point_to_rotate = (-3, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, (2*math.pi) - (math.pi / 4))
        self.assertAlmostEqual(0, new_point[0], places=4)
        self.assertAlmostEqual(4.2426, new_point[1], places=4)

    def test_rotate3(self):
        center = (0, 0)
        point_to_rotate = (-4, 2)
        new_point = Geometrics.rotate(center, point_to_rotate, (math.pi / 3.3879099684))
        self.assertAlmostEqual(-4, new_point[0], places=4)
        self.assertAlmostEqual(-2, new_point[1], places=4)

    def test_rotate4(self):
        center = (0, 0)
        point_to_rotate = (-4, 2)
        new_point = Geometrics.rotate(center, point_to_rotate, (2*math.pi) - (math.pi / 3.3879099684))
        self.assertAlmostEqual(-0.8, new_point[0], places=4)
        self.assertAlmostEqual(4.4, new_point[1], places=4)

    def test_rotate5(self):
        center = (-1, 1)
        point_to_rotate = (-5, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, (math.pi / 3.3879099684))
        self.assertAlmostEqual(-5, new_point[0], places=4)
        self.assertAlmostEqual(-1, new_point[1], places=4)

    def test_rotate6(self):
        center = (-1, 1)
        point_to_rotate = (-5, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, (2*math.pi) - (math.pi / 3.3879099684))
        self.assertAlmostEqual(-1.8, new_point[0], places=4)
        self.assertAlmostEqual(5.4, new_point[1], places=4)

    def test_resize1(self):
        center = (0, 0)
        point_to_move = (-3, 3)
        new_point = Geometrics.resize(center, point_to_move, 2)
        self.assertAlmostEqual(-6, new_point[0], places=4)
        self.assertAlmostEqual(6, new_point[1], places=4)

    def test_resize2(self):
        center = (-1, 1)
        point_to_move = (-3, 3)
        new_point = Geometrics.resize(center, point_to_move, 2)
        self.assertAlmostEqual(-5, new_point[0], places=4)
        self.assertAlmostEqual(5, new_point[1], places=4)


if __name__ == '__main__':
    unittest.main()

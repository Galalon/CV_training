import unittest

from OOP.OOP_EX.OOP_EX.ParsersAndDrawers.JSONParser import JSONParser


class JSONParserTest(unittest.TestCase):
    def test_house_json(self):
        parser = JSONParser()
        shape = parser.parse('../DataForTest/House.json')
        self.assertEqual(-160, shape._child_shapes[0]._points[0][0])
        self.assertEqual(-55, shape._child_shapes[0]._points[0][1])
        self.assertEqual(160, shape._child_shapes[0]._points[1][0])
        self.assertEqual(-55, shape._child_shapes[0]._points[1][1])
        self.assertEqual(0, shape._child_shapes[0]._points[2][0])
        self.assertEqual(-265, shape._child_shapes[0]._points[2][1])


if __name__ == '__main__':
    unittest.main()

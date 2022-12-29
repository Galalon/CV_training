import copy
from typing import Dict

from OOP.OOP_EX.OOP_EX.Shapes.Circle import Circle
from OOP.OOP_EX.OOP_EX.Shapes.CompositeShape import CompositeShape
from OOP.OOP_EX.OOP_EX.Shapes.Line import Line
from OOP.OOP_EX.OOP_EX.Shapes.Point import Point
from OOP.OOP_EX.OOP_EX.Shapes.Rectangle import Rectangle
from OOP.OOP_EX.OOP_EX.Shapes.Shape import Shape
from OOP.OOP_EX.OOP_EX.Shapes.Triangle import Triangle


class ShapeFactoryFromJSON:

    def __init__(self):
        self._name_to_class_map = dict(Point=Point, Line=Line, Triangle=Triangle, Rectangle=Rectangle, Circle=Circle)

    def build_shape_from_json(self, json_dict: Dict) -> Shape:
        """

        :param json_dict: the json dictionary that describes the shape to build
        :return: A Shape object corresponding to the json dictionary
        """
        shape_name = json_dict['shapeName']
        json_dict_new = self.__pop_unrelated_keys(json_dict)
        if shape_name in self._name_to_class_map.keys():
            shape = self._name_to_class_map[shape_name](**json_dict_new)
            return shape
        else:
            shape = CompositeShape()
            return shape

    @staticmethod
    def __pop_unrelated_keys(json_dict: Dict) -> Dict:
        """
        Auxiliary method to clear unnecessary keys that are not needed to build the object
        :param json_dict: Json dictionary to delete keys from
        :return: a new dict without the unnecessary keys
        """
        json_dict_copy = copy.deepcopy(json_dict)
        json_dict_copy.pop('shapeName', None)
        json_dict_copy.pop('translationX', None)
        json_dict_copy.pop('translationY', None)
        json_dict_copy.pop('rotate_angle', None)
        json_dict_copy.pop('resize', None)
        return json_dict_copy
